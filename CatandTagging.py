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

class TaskWithCategoriesAndTags(Task):
    """
    Extends the Task class to include categories and tags.
    Attributes:
        category (str): The category of the task.
        tags (list): A list of tags associated with the task.
    """
    def __init__(self, title: str, description: str, status: str = "incomplete", category: str = None, tags: list = None):
        """
        Initializes a new TaskWithCategoriesAndTags instance.
        Args:
            title (str): The title of the task.
            description (str): A brief description of the task.
            status (str): The initial status of the task (default is "incomplete").
            category (str): The category of the task (optional).
            tags (list): A list of tags associated with the task (optional).
        """
        super().__init__(title, description, status)
        self.category = category
        self.tags = tags or []

class TaskManagerWithCategoriesAndTags(TaskManager):
    """
    Extends TaskManager to add functionality for managing categories and tags.
    """
    def add_task(self, title: str, description: str, category: str = None, tags: list = None):
        """
        Adds a new task with a category and tags to the task list.
        Args:
            title (str): The title of the task.
            description (str): A brief description of the task.
            category (str): The category of the task (optional).
            tags (list): A list of tags associated with the task (optional).
        """
        task = TaskWithCategoriesAndTags(title, description, category=category, tags=tags)
        self.tasks.append(task)

    def filter_tasks_by_category(self, category: str):
        """
        Filters tasks based on their category.
        Args:
            category (str): The category to filter by.
        Returns:
            list: A list of tasks matching the specified category.
        """
        return [task for task in self.tasks if isinstance(task, TaskWithCategoriesAndTags) and task.category == category]

    def search_tasks_by_tags(self, tags: list):
        """
        Searches for tasks that contain any of the specified tags.
        Args:
            tags (list): A list of tags to search for.
        Returns:
            list: A list of tasks containing any of the specified tags.
        """
        return [
            task for task in self.tasks
            if isinstance(task, TaskWithCategoriesAndTags) and any(tag in task.tags for tag in tags)
        ]

    def filter_tasks_by_nested_category(self, category_hierarchy: list):
        """
        Filters tasks based on a nested category hierarchy.
        Args:
            category_hierarchy (list): A list representing the category hierarchy (e.g., ["Work", "Project A"]).
        Returns:
            list: A list of tasks matching the specified nested category.
        """
        return [
            task for task in self.tasks
            if isinstance(task, TaskWithCategoriesAndTags) and task.category and task.category.split("/") == category_hierarchy
        ]


