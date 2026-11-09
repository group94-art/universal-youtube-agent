# Architecture

## Execution flow
Command -> identity/workspace -> channel context -> intent parser -> planner -> skill dependency graph -> policy check -> worker -> output validation -> persistence -> report.

Long-running tasks are asynchronous, resumable, observable, and idempotent where possible. Independent research tasks can run concurrently; media steps follow explicit dependencies.

## Services
- API gateway: authentication, workspace scoping, validation, rate limits.
- Orchestrator: command interpretation, planning, skill selection, task state.
- Skill runtime: versioned manifests, schemas, permissions, timeouts.
- Workers: research, media processing, analytics sync, scheduled jobs.
- Policy engine: approvals, spend limits, channel scope, destructive-action guardrails.
- Memory: channel facts/preferences/results with provenance and retention.
- Provider adapters: LLM, search, TTS, image/video generation, transcription, storage.
- YouTube integration: OAuth, token refresh, channel discovery, uploads, analytics.

## Domain model
users, workspaces, memberships, channels, channel_profiles, integrations, skills, skill_versions, workflows, tasks, task_events, content_ideas, scripts, media_assets, videos, publishing_jobs, analytics_snapshots, channel_memory, approvals, usage_ledger, audit_events.

Every tenant-owned record must be workspace-scoped. Encrypt credentials at rest and never return them to the browser.

## Media workflow
Brief -> research -> script -> storyboard -> voiceover -> visuals -> assembly -> captions -> thumbnail -> quality checks -> export -> approval -> upload/schedule.

Provider interfaces allow vendor replacement. Validate file type, duration, dimensions, audio, storage limits, and asset provenance.

## Reliability
Use idempotency keys, bounded retries, exponential backoff, dead-letter handling, cancellation, task leases, and explicit partial-failure states. Reconcile upload status before retrying a publish.

## Deployment
Dockerized API, workers, scheduler, PostgreSQL, Redis, object storage, and web frontend. Production migrations, OAuth verification, backups, and deployment are separate milestones.
