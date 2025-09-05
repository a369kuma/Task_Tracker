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

import argparse
import json

class CommandLineInterface:
    """
    Provides a command-line interface for interacting with the task manager.
    Includes support for configuration files and argument validation.
    """
    def __init__(self, task_manager: TaskManager):
        """
        Initializes the command-line interface.
        Args:
            task_manager (TaskManager): An instance of TaskManager to manage tasks.
        """
        self.task_manager = task_manager

    # Expansion A: Configuration File Support
    def load_config(self, config_file: str):
        """
        Loads settings from a configuration file.
        Args:
            config_file (str): The path to the configuration file (JSON format).
        """
        if not os.path.exists(config_file):
            print(f"Configuration file '{config_file}' not found.")
            return

        with open(config_file, "r") as file:
            config = json.load(file)
            for task in config.get("tasks", []):
                self.task_manager.add_task(task["title"], task["description"])
            print(f"Loaded {len(config.get('tasks', []))} tasks from configuration file.")

    # Expansion B: Argument Validation
    def validate_arguments(self, args):
        """
        Validates the command-line arguments.
        Args:
            args (argparse.Namespace): Parsed command-line arguments.
        """
        if args.command not in ["add", "remove", "list", "complete", "incomplete"]:
            print(f"Invalid command: {args.command}")
            print("Valid commands are: add, remove, list, complete, incomplete.")
            exit(1)

    def execute(self, args):
        """
        Executes the command based on the parsed arguments.
        Args:
            args (argparse.Namespace): Parsed command-line arguments.
        """
        self.validate_arguments(args)

        if args.command == "add":
            self.task_manager.add_task(args.title, args.description)
            print(f"Task '{args.title}' added successfully.")
        elif args.command == "remove":
            self.task_manager.remove_task(args.title)
            print(f"Task '{args.title}' removed successfully.")
        elif args.command == "list":
            print("Listing all tasks:")
            self.task_manager.list_tasks()
        elif args.command == "complete":
            self.task_manager.mark_task_complete(args.title)
            print(f"Task '{args.title}' marked as complete.")
        elif args.command == "incomplete":
            self.task_manager.mark_task_incomplete(args.title)
            print(f"Task '{args.title}' marked as incomplete.")


