-- Initial tenant-aware domain schema. Run only after provisioning PostgreSQL.
CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE workspaces (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  name varchar(120) NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE memberships (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  workspace_id uuid NOT NULL REFERENCES workspaces(id) ON DELETE CASCADE,
  user_subject varchar(255) NOT NULL,
  role varchar(32) NOT NULL DEFAULT 'owner',
  created_at timestamptz NOT NULL DEFAULT now(),
  CONSTRAINT uq_membership_workspace_user UNIQUE(workspace_id, user_subject)
);

CREATE TABLE channels (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  workspace_id uuid NOT NULL REFERENCES workspaces(id) ON DELETE CASCADE,
  platform varchar(32) NOT NULL DEFAULT 'youtube' CHECK (platform = 'youtube'),
  external_channel_id varchar(128) NOT NULL,
  title varchar(200) NOT NULL,
  niche varchar(160),
  created_at timestamptz NOT NULL DEFAULT now(),
  CONSTRAINT uq_channel_workspace_external UNIQUE(workspace_id, platform, external_channel_id)
);

CREATE TYPE task_state AS ENUM ('queued','running','waiting_approval','succeeded','failed','cancelled');
CREATE TABLE agent_tasks (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  workspace_id uuid NOT NULL REFERENCES workspaces(id) ON DELETE CASCADE,
  channel_id uuid REFERENCES channels(id) ON DELETE SET NULL,
  task_type varchar(80) NOT NULL,
  status task_state NOT NULL DEFAULT 'queued',
  input_payload jsonb NOT NULL DEFAULT '{}'::jsonb,
  output_payload jsonb,
  idempotency_key varchar(128) NOT NULL,
  error_code varchar(80),
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  CONSTRAINT uq_task_workspace_idempotency UNIQUE(workspace_id, idempotency_key)
);
CREATE INDEX ix_agent_tasks_workspace_status_created ON agent_tasks(workspace_id, status, created_at DESC);

CREATE TABLE task_events (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  workspace_id uuid NOT NULL REFERENCES workspaces(id) ON DELETE CASCADE,
  task_id uuid NOT NULL REFERENCES agent_tasks(id) ON DELETE CASCADE,
  event_type varchar(80) NOT NULL,
  detail text,
  created_at timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX ix_task_events_workspace_task ON task_events(workspace_id, task_id, created_at);

CREATE TABLE audit_events (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  workspace_id uuid NOT NULL REFERENCES workspaces(id) ON DELETE CASCADE,
  actor_subject varchar(255) NOT NULL,
  action varchar(100) NOT NULL,
  resource_type varchar(80) NOT NULL,
  resource_id varchar(128),
  created_at timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX ix_audit_events_workspace_created ON audit_events(workspace_id, created_at DESC);

-- Application must verify workspace membership on every read/write.
-- Do not expose these tables through an unauthenticated API.
