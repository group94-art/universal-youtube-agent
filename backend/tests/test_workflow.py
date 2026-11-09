import pytest

from app.core.workflow import InvalidTaskTransition, TaskStatus, transition


def test_queued_task_can_start_or_cancel():
    assert transition(TaskStatus.QUEUED, TaskStatus.RUNNING) is TaskStatus.RUNNING
    assert transition(TaskStatus.QUEUED, TaskStatus.CANCELLED) is TaskStatus.CANCELLED


def test_running_task_can_wait_for_approval_or_finish():
    assert transition(TaskStatus.RUNNING, TaskStatus.WAITING_APPROVAL) is TaskStatus.WAITING_APPROVAL
    assert transition(TaskStatus.RUNNING, TaskStatus.SUCCEEDED) is TaskStatus.SUCCEEDED


def test_failed_task_can_be_requeued():
    assert transition(TaskStatus.FAILED, TaskStatus.QUEUED) is TaskStatus.QUEUED


@pytest.mark.parametrize("target", [TaskStatus.RUNNING, TaskStatus.SUCCEEDED, TaskStatus.FAILED])
def test_terminal_success_cannot_transition(target):
    with pytest.raises(InvalidTaskTransition):
        transition(TaskStatus.SUCCEEDED, target)


def test_waiting_approval_cannot_start_without_explicit_requeue():
    with pytest.raises(InvalidTaskTransition):
        transition(TaskStatus.WAITING_APPROVAL, TaskStatus.RUNNING)
