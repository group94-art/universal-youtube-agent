"""Small, deterministic workflow state machine.

External side effects are deliberately outside this module. Callers must apply
authorization and approval policy before invoking integrations.
"""
from enum import StrEnum


class TaskStatus(StrEnum):
    QUEUED = "queued"
    RUNNING = "running"
    WAITING_APPROVAL = "waiting_approval"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELLED = "cancelled"


TERMINAL_STATUSES = {TaskStatus.SUCCEEDED, TaskStatus.FAILED, TaskStatus.CANCELLED}

_ALLOWED: dict[TaskStatus, set[TaskStatus]] = {
    TaskStatus.QUEUED: {TaskStatus.RUNNING, TaskStatus.CANCELLED},
    TaskStatus.RUNNING: {
        TaskStatus.WAITING_APPROVAL,
        TaskStatus.SUCCEEDED,
        TaskStatus.FAILED,
        TaskStatus.CANCELLED,
    },
    TaskStatus.WAITING_APPROVAL: {
        TaskStatus.QUEUED,
        TaskStatus.CANCELLED,
    },
    TaskStatus.SUCCEEDED: set(),
    TaskStatus.FAILED: {TaskStatus.QUEUED},
    TaskStatus.CANCELLED: set(),
}


class InvalidTaskTransition(ValueError):
    pass


def transition(current: TaskStatus, target: TaskStatus) -> TaskStatus:
    """Validate and return a new state; never performs an external action."""
    if target not in _ALLOWED[current]:
        raise InvalidTaskTransition(f"Cannot transition task from {current} to {target}")
    return target
