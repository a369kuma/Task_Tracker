# Import the classes to be tested
from Data_Persistance import Task, TaskManager

def test_task_class():
    # Test Task initialization
    task = Task("Test Task", "This is a test task.")
    assert task.title == "Test Task"
    assert task.description == "This is a test task."
    assert task.status == "incomplete"

    # Test mark_complete and mark_incomplete methods
    task.mark_complete()
    assert task.status == "complete"
    task.mark_incomplete()
    assert task.status == "incomplete"

def test_task_manager_class():
    manager = TaskManager()

    # Test adding tasks
    manager.add_task("Task 1", "Description 1")
    manager.add_task("Task 2", "Description 2")
    assert len(manager.tasks) == 2

    # Test listing tasks
    manager.list_tasks()  # Should print details of Task 1 and Task 2

    # Test marking tasks as complete
    manager.mark_task_complete("Task 1")
    assert manager.tasks[0].status == "complete"

    # Test marking tasks as incomplete
    manager.mark_task_incomplete("Task 1")
    assert manager.tasks[0].status == "incomplete"

    # Test removing tasks
    manager.remove_task("Task 1")
    assert len(manager.tasks) == 1
    assert manager.tasks[0].title == "Task 2"

    # Test removing a non-existent task
    manager.remove_task("Non-existent Task")  # Should not raise an error
    assert len(manager.tasks) == 1

    # Test marking a non-existent task as complete
    manager.mark_task_complete("Non-existent Task")  # Should not raise an error

    # Test marking a non-existent task as incomplete
    manager.mark_task_incomplete("Non-existent Task")  # Should not raise an error

if __name__ == "__main__":
    print("Running tests...")
    test_task_class()
    test_task_manager_class()
    print("All tests passed!")
