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





class AdvancedTaskManager(TaskManager):
    """
    Extends TaskManager to add advanced querying functionality, including filtering by status,
    searching by keywords, multi-criteria filtering, and searching by multiple keywords.
    """
    def filter_tasks_by_status(self, status: str):
        """
        Filters tasks based on their status (complete/incomplete).
        Args:
            status (str): The status to filter by ("complete" or "incomplete").
        Returns:
            list: A list of tasks matching the specified status.
        """
        return [task for task in self.tasks if task.status == status]

    def search_tasks_by_keyword(self, keyword: str):
        """
        Searches for tasks that contain the specified keyword in their title or description.
        Args:
            keyword (str): The keyword to search for.
        Returns:
            list: A list of tasks containing the keyword.
        """
        return [task for task in self.tasks if keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower()]

    # Multi-criteria Filtering
    def filter_tasks(self, status: str = None, keywords: list = None):
        """
        Filters tasks based on multiple criteria, such as status and keywords.
        Args:
            status (str): The status to filter by ("complete" or "incomplete"). Optional.
            keywords (list): A list of keywords to search for in the title or description. Optional.
        Returns:
            list: A list of tasks matching the specified criteria.
        """
        filtered_tasks = self.tasks

        if status:
            filtered_tasks = [task for task in filtered_tasks if task.status == status]

        if keywords:
            filtered_tasks = [
                task for task in filtered_tasks
                if any(keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower() for keyword in keywords)
            ]

        return filtered_tasks

    # Search by Multiple Keywords
    def search_tasks_by_keywords(self, keywords: list):
        """
        Searches for tasks that contain any of the specified keywords in their title or description.
        Args:
            keywords (list): A list of keywords to search for.
        Returns:
            list: A list of tasks containing any of the keywords.
        """
        return [
            task for task in self.tasks
            if any(keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower() for keyword in keywords)
        ]






