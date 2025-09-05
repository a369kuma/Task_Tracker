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

class User:
    """
    Represents a user in the task management system.
    Attributes:
        username (str): The username of the user.
        tasks (TaskManager): The task manager for the user's tasks.
    """
    def __init__(self, username: str):
        """
        Initializes a new User instance.
        Args:
            username (str): The username of the user.
        """
        self.username = username
        self.tasks = TaskManager()

class CollaborationManager:
    """
    Manages collaboration between users, including task sharing and permissions.
    Attributes:
        users (dict): A dictionary of users, keyed by their username.
    """
    def __init__(self):
        """
        Initializes a new CollaborationManager instance.
        """
        self.users = {}

    def add_user(self, username: str):
        """
        Adds a new user to the system.
        Args:
            username (str): The username of the user to add.
        """
        if username in self.users:
            print(f"User '{username}' already exists.")
        else:
            self.users[username] = User(username)
            print(f"User '{username}' added successfully.")

    # Expansion A: User Permissions
    def share_task(self, from_user: str, to_user: str, task_title: str, permission: str = "read"):
        """
        Shares a task from one user to another with specified permissions.
        Args:
            from_user (str): The username of the user sharing the task.
            to_user (str): The username of the user receiving the task.
            task_title (str): The title of the task to share.
            permission (str): The permission level ("read" or "edit").
        """
        if from_user not in self.users or to_user not in self.users:
            print("Both users must exist to share a task.")
            return

        from_user_tasks = self.users[from_user].tasks
        to_user_tasks = self.users[to_user].tasks

        task_to_share = next((task for task in from_user_tasks.tasks if task.title == task_title), None)
        if not task_to_share:
            print(f"Task '{task_title}' not found for user '{from_user}'.")
            return

        shared_task = Task(task_to_share.title, task_to_share.description, task_to_share.status)
        if permission == "read":
            shared_task.mark_complete = lambda: print("Permission denied: Read-only access.")
            shared_task.mark_incomplete = lambda: print("Permission denied: Read-only access.")
        to_user_tasks.tasks.append(shared_task)
        print(f"Task '{task_title}' shared from '{from_user}' to '{to_user}' with '{permission}' permission.")

    # Expansion B: Task Comments
    def add_comment_to_task(self, username: str, task_title: str, comment: str):
        """
        Adds a comment to a task for a specific user.
        Args:
            username (str): The username of the user whose task will be commented on.
            task_title (str): The title of the task to comment on.
            comment (str): The comment to add.
        """
        if username not in self.users:
            print(f"User '{username}' does not exist.")
            return

        user_tasks = self.users[username].tasks
        task_to_comment = next((task for task in user_tasks.tasks if task.title == task_title), None)
        if not task_to_comment:
            print(f"Task '{task_title}' not found for user '{username}'.")
            return

        if not hasattr(task_to_comment, "comments"):
            task_to_comment.comments = []
        task_to_comment.comments.append(comment)
        print(f"Comment added to task '{task_title}' for user '{username}'.")



