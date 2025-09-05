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

class TaskManagerWithHistory(TaskManager):
    """
    Extends TaskManager to include undo and redo functionality.
    """
    def __init__(self):
        """
        Initializes a new TaskManagerWithHistory instance with undo and redo stacks.
        """
        super().__init__()
        self.history = []  # Stack to store previous states for undo
        self.redo_stack = []  # Stack to store states for redo

    # Expansion A: Multi-step Undo
    def save_state(self):
        """
        Saves the current state of the task list to the history stack.
        """
        self.history.append([task.__dict__.copy() for task in self.tasks])
        self.redo_stack.clear()  # Clear redo stack whenever a new operation is performed

    def undo(self):
        """
        Reverts the task list to the last saved state.
        Raises:
            IndexError: If there is no state to undo.
        """
        if not self.history:
            print("No actions to undo.")
            return
        self.redo_stack.append([task.__dict__.copy() for task in self.tasks])
        previous_state = self.history.pop()
        self.tasks = [Task(**task) for task in previous_state]
        print("Undo successful.")

    # Expansion B: Redo Functionality
    def redo(self):
        """
        Reapplies the last undone state to the task list.
        Raises:
            IndexError: If there is no state to redo.
        """
        if not self.redo_stack:
            print("No actions to redo.")
            return
        self.history.append([task.__dict__.copy() for task in self.tasks])
        next_state = self.redo_stack.pop()
        self.tasks = [Task(**next_state) for next_state in next_state]
        print("Redo successful.")

    # Override methods to include state saving
    def add_task(self, title: str, description: str):
        self.save_state()
        super().add_task(title, description)

    def remove_task(self, title: str):
        self.save_state()
        super().remove_task(title)

    def mark_task_complete(self, title: str):
        self.save_state()
        super().mark_task_complete(title)

    def mark_task_incomplete(self, title: str):
        self.save_state()
        super().mark_task_incomplete(title)


