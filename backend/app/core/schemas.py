from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from app.core.workflow import TaskStatus


class WorkspaceCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)


class ChannelCreate(BaseModel):
    platform: str = Field(default="youtube", pattern="^youtube$")
    external_channel_id: str = Field(min_length=1, max_length=128)
    title: str = Field(min_length=1, max_length=200)
    niche: str | None = Field(default=None, max_length=160)


class TaskCreate(BaseModel):
    workspace_id: UUID
    channel_id: UUID | None = None
    task_type: str = Field(min_length=2, max_length=80)
    input: dict = Field(default_factory=dict)
    idempotency_key: str = Field(min_length=8, max_length=128)


class TaskRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    workspace_id: UUID
    channel_id: UUID | None
    task_type: str
    status: TaskStatus
    created_at: datetime
