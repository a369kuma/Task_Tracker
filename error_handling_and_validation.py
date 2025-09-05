# This module defines a simple task tracking system. It includes a Task class to represent individual tasks
# and a TaskManager class to manage a collection of tasks. Tasks have a title, description, and status
# (either "incomplete" or "complete"). The TaskManager provides methods to add, remove, list tasks, and
# update their status.

import json
import os
from datetime import datetime

# import logging

# # Set up logging
# logging.basicConfig(
#     filename="task_manager.log",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )

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

# # Custom Exceptions
# class TaskNotFoundError(Exception):
#     """Raised when a task is not found in the task list."""
#     pass

# class InvalidInputError(Exception):
#     """Raised when user input is invalid."""
#     pass

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




class TaskManagerWithValidation(TaskManager):
    """
    Extends TaskManager to include error handling, input validation, and logging.
    """
    def add_task(self, title: str, description: str):
        """
        Adds a new task to the task list with input validation.
        Args:
            title (str): The title of the task.
            description (str): A brief description of the task.
        Raises:
            InvalidInputError: If the title or description is empty.
        """
        if not title.strip() or not description.strip():
            logging.error("Failed to add task: Title or description is empty.")
            raise InvalidInputError("Task title and description cannot be empty.")
        super().add_task(title, description)
        logging.info(f"Task added: {title}")

    def remove_task(self, title: str):
        """
        Removes a task from the task list with error handling.
        Args:
            title (str): The title of the task to be removed.
        Raises:
            TaskNotFoundError: If the task with the given title does not exist.
        """
        task_titles = [task.title for task in self.tasks]
        if title not in task_titles:
            logging.error(f"Failed to remove task: Task '{title}' not found.")
            raise TaskNotFoundError(f"Task with title '{title}' not found.")
        super().remove_task(title)
        logging.info(f"Task removed: {title}")

    def mark_task_complete(self, title: str):
        """
        Marks a task as complete with error handling.
        Args:
            title (str): The title of the task to be marked as complete.
        Raises:
            TaskNotFoundError: If the task with the given title does not exist.
        """
        task_titles = [task.title for task in self.tasks]
        if title not in task_titles:
            logging.error(f"Failed to mark task as complete: Task '{title}' not found.")
            raise TaskNotFoundError(f"Task with title '{title}' not found.")
        super().mark_task_complete(title)
        logging.info(f"Task marked as complete: {title}")

    def mark_task_incomplete(self, title: str):
        """
        Marks a task as incomplete with error handling.
        Args:
            title (str): The title of the task to be marked as incomplete.
        Raises:
            TaskNotFoundError: If the task with the given title does not exist.
        """
        task_titles = [task.title for task in self.tasks]
        if title not in task_titles:
            logging.error(f"Failed to mark task as incomplete: Task '{title}' not found.")
            raise TaskNotFoundError(f"Task with title '{title}' not found.")
        super().mark_task_incomplete(title)
        logging.info(f"Task marked as incomplete: {title}")

    def list_tasks(self):
        """
        Lists all tasks with logging.
        """
        if not self.tasks:
            logging.info("No tasks to list.")
            print("No tasks available.")
        else:
            logging.info("Listing all tasks.")
            super().list_tasks()






