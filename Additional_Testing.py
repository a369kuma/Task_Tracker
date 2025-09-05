# This module defines a simple task tracking system. It includes a Task class to represent individual tasks
# and a TaskManager class to manage a collection of tasks. Tasks have a title, description, and status
# (either "incomplete" or "complete"). The TaskManager provides methods to add, remove, list tasks, and
# update their status.

import json
import os
from datetime import datetime

class Task:
    """
    Represents an individual task with a title, description, and status.
    Attributes:
        title (str): The title of the task.
        description (str): A brief description of the task.
        status (str): The status of the task, either "incomplete" or "complete".
    """
    def __init__(self, title: str, description: str, status: str = "incomplete"):
        """
        Initializes a new Task instance.
        Args:
            title (str): The title of the task.
            description (str): A brief description of the task.
            status (str): The initial status of the task (default is "incomplete").
        """
        self.title = title
        self.description = description
        self.status = status

    def mark_complete(self):
        """
        Marks the task as complete by setting its status to "complete".
        """
        self.status = "complete"

    def mark_incomplete(self):
        """
        Marks the task as incomplete by setting its status to "incomplete".
        """
        self.status = "incomplete"

class TaskManager:
    """
    Manages a collection of tasks, providing methods to add, remove, list, and update tasks.
    Attributes:
        tasks (list): A list of Task objects being managed.
    """
    def __init__(self):
        """
        Initializes a new TaskManager instance with an empty task list.
        """
        self.tasks = []

    def add_task(self, title: str, description: str):
        """
        Adds a new task to the task list.
        Args:
            title (str): The title of the task.
            description (str): A brief description of the task.
        """
        task = Task(title, description)
        self.tasks.append(task)

    def remove_task(self, title: str):
        """
        Removes a task from the task list based on its title.
        Args:
            title (str): The title of the task to be removed.
        """
        self.tasks = [task for task in self.tasks if task.title != title]

    def list_tasks(self):
        """
        Lists all tasks in the task list, displaying their title, description, and status.
        """
        for task in self.tasks:
            print(f"Title: {task.title}, Description: {task.description}, Status: {task.status}")

    def mark_task_complete(self, title: str):
        """
        Marks a task as complete based on its title.
        Args:
            title (str): The title of the task to be marked as complete.
        """
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()

    def mark_task_incomplete(self, title: str):
        """
        Marks a task as incomplete based on its title.
        Args:
            title (str): The title of the task to be marked as incomplete.
        """
        for task in self.tasks:
            if task.title == title:
                task.mark_incomplete()





import unittest
from unittest.mock import MagicMock
from datetime import datetime, timedelta
from Task import Task, TaskManager, TaskWithDueDateAndPriority, TaskManagerWithDueDatesAndSorting

class TestTask(unittest.TestCase):
    """
    Unit tests for the Task class.
    """
    def test_task_initialization(self):
        task = Task("Test Task", "This is a test task.")
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "This is a test task.")
        self.assertEqual(task.status, "incomplete")

    def test_mark_complete(self):
        task = Task("Test Task", "This is a test task.")
        task.mark_complete()
        self.assertEqual(task.status, "complete")

    def test_mark_incomplete(self):
        task = Task("Test Task", "This is a test task.", status="complete")
        task.mark_incomplete()
        self.assertEqual(task.status, "incomplete")

class TestTaskManager(unittest.TestCase):
    """
    Unit tests for the TaskManager class.
    """
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        self.manager.add_task("Task 1", "Description 1")
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0].title, "Task 1")

    def test_remove_task(self):
        self.manager.add_task("Task 1", "Description 1")
        self.manager.remove_task("Task 1")
        self.assertEqual(len(self.manager.tasks), 0)

    def test_list_tasks(self):
        self.manager.add_task("Task 1", "Description 1")
        self.manager.add_task("Task 2", "Description 2")
        with unittest.mock.patch('builtins.print') as mocked_print:
            self.manager.list_tasks()
            mocked_print.assert_any_call("Title: Task 1, Description: Description 1, Status: incomplete")
            mocked_print.assert_any_call("Title: Task 2, Description: Description 2, Status: incomplete")

class TestTaskWithDueDateAndPriority(unittest.TestCase):
    """
    Unit tests for the TaskWithDueDateAndPriority class.
    """
    def test_due_date_initialization(self):
        task = TaskWithDueDateAndPriority("Task 1", "Description 1", due_date="2023-10-15", priority="high")
        self.assertEqual(task.due_date, datetime.strptime("2023-10-15", "%Y-%m-%d"))
        self.assertEqual(task.priority, "high")

    def test_is_due_soon(self):
        task = TaskWithDueDateAndPriority("Task 1", "Description 1", due_date=(datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d"))
        self.assertTrue(task.is_due_soon())

# Expansion A: Mocking Dependencies
class TestMocking(unittest.TestCase):
    """
    Tests using mocking to isolate functionality.
    """
    def test_mock_task_manager(self):
        """
        Tests the add_task method using a mocked TaskManager.
        """
        mock_manager = MagicMock(spec=TaskManager)
        mock_manager.add_task("Mock Task", "Mock Description")
        mock_manager.add_task.assert_called_with("Mock Task", "Mock Description")

# Expansion B: Performance Testing
class TestPerformance(unittest.TestCase):
    """
    Performance tests for the task management system.
    """
    def test_large_number_of_tasks(self):
        """
        Tests the system's ability to handle a large number of tasks.
        """
        manager = TaskManager()
        for i in range(10000):
            manager.add_task(f"Task {i}", f"Description {i}")
        self.assertEqual(len(manager.tasks), 10000)

    def test_sorting_performance(self):
        """
        Tests the performance of sorting tasks by due date with a large number of tasks.
        """
        manager = TaskManagerWithDueDatesAndSorting()
        for i in range(10000):
            manager.add_task(f"Task {i}", f"Description {i}", due_date=(datetime.now() + timedelta(days=i % 30)).strftime("%Y-%m-%d"))
        manager.sort_tasks_by_due_date()
        self.assertTrue(all(manager.tasks[i].due_date <= manager.tasks[i + 1].due_date for i in range(len(manager.tasks) - 1)))

if __name__ == "__main__":
    unittest.main()