# This module defines a simple task tracking system. It includes a Task class to represent individual tasks
# and a TaskManager class to manage a collection of tasks. Tasks have a title, description, and status
# (either "incomplete" or "complete"). The TaskManager provides methods to add, remove, list tasks, and
# update their status.

import json
import os
from datetime import datetime, timedelta

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

class TaskWithDueDateAndPriority(Task):
    """
    Extends the Task class to include due dates and priority levels.
    Attributes:
        due_date (datetime): The due date of the task.
        priority (str): The priority level of the task ("low", "medium", "high").
    """
    def __init__(self, title: str, description: str, status: str = "incomplete", due_date: str = None, priority: str = "medium"):
        """
        Initializes a new TaskWithDueDateAndPriority instance.
        Args:
            title (str): The title of the task.
            description (str): A brief description of the task.
            status (str): The initial status of the task (default is "incomplete").
            due_date (str): The due date of the task in "YYYY-MM-DD" format (optional).
            priority (str): The priority level of the task (default is "medium").
        """
        super().__init__(title, description, status)
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d") if due_date else None
        self.priority = priority

    def is_due_soon(self, days: int = 3):
        """
        Checks if the task is due within the specified number of days.
        Args:
            days (int): The number of days to check for upcoming due dates.
        Returns:
            bool: True if the task is due soon, False otherwise.
        """
        if self.due_date:
            return datetime.now() + timedelta(days=days) >= self.due_date
        return False

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





class TaskManagerWithDueDatesAndSorting(TaskManager):
    """
    Extends TaskManager to add functionality for due dates, sorting, reminders, and priority levels.
    """
    def add_task(self, title: str, description: str, due_date: str = None, priority: str = "medium"):
        """
        Adds a new task with a due date and priority level to the task list.
        Args:
            title (str): The title of the task.
            description (str): A brief description of the task.
            due_date (str): The due date of the task in "YYYY-MM-DD" format (optional).
            priority (str): The priority level of the task (default is "medium").
        """
        task = TaskWithDueDateAndPriority(title, description, due_date=due_date, priority=priority)
        self.tasks.append(task)

    def sort_tasks_by_due_date(self):
        """
        Sorts tasks by their due date in ascending order. Tasks without a due date are placed at the end.
        """
        self.tasks.sort(key=lambda task: task.due_date or datetime.max)

    def sort_tasks_by_priority(self):
        """
        Sorts tasks by their priority level in the order: high, medium, low.
        """
        priority_order = {"high": 1, "medium": 2, "low": 3}
        self.tasks.sort(key=lambda task: priority_order.get(task.priority, 4))

    def sort_tasks_by_status(self):
        """
        Sorts tasks by their status, placing "incomplete" tasks before "complete" tasks.
        """
        self.tasks.sort(key=lambda task: task.status)

    def list_due_soon_tasks(self, days: int = 3):
        """
        Lists tasks that are due within the specified number of days.
        Args:
            days (int): The number of days to check for upcoming due dates.
        """
        due_soon_tasks = [task for task in self.tasks if isinstance(task, TaskWithDueDateAndPriority) and task.is_due_soon(days)]
        for task in due_soon_tasks:
            print(f"Title: {task.title}, Due Date: {task.due_date.strftime('%Y-%m-%d')}, Priority: {task.priority}")

# Example usage:
if __name__ == "__main__":
    manager = TaskManagerWithDueDatesAndSorting()
    manager.add_task("Complete project", "Finish the project by the end of the week.", due_date="2023-10-15", priority="high")
    manager.add_task("Buy groceries", "Get milk, eggs, and bread.", due_date="2023-10-10", priority="medium")
    manager.add_task("Workout", "Go for a run in the morning.", priority="low")

    print("Tasks sorted by due date:")
    manager.sort_tasks_by_due_date()
    manager.list_tasks()

    print("\nTasks sorted by priority:")
    manager.sort_tasks_by_priority()
    manager.list_tasks()

    print("\nTasks due soon:")
    manager.list_due_soon_tasks(days=5)

