# This module defines a simple task tracking system. It includes a Task class to represent individual tasks
# and a TaskManager class to manage a collection of tasks. Tasks have a title, description, and status
# (either "incomplete" or "complete"). The TaskManager provides methods to add, remove, list tasks, and
# update their status.

import json
import os
from datetime import datetime
from collections import deque

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

class ConsoleInterface:
    """
    Provides a menu-driven console interface for interacting with the task manager.
    Includes command history and theming options.
    """
    def __init__(self, task_manager: TaskManager):
        """
        Initializes the console interface.
        Args:
            task_manager (TaskManager): An instance of TaskManager to manage tasks.
        """
        self.task_manager = task_manager
        self.command_history = deque(maxlen=50)  # Stores the last 50 commands
        self.theme = "default"  # Default theme

    def display_menu(self):
        """
        Displays the main menu options to the user.
        """
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Mark Task as Complete")
        print("5. Mark Task as Incomplete")
        print("6. View Command History")
        print("7. Change Theme")
        print("8. Exit")

    def execute_command(self, command: str):
        """
        Executes a command based on user input.
        Args:
            command (str): The command entered by the user.
        """
        self.command_history.append(command)  # Save command to history

        if command == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            self.task_manager.add_task(title, description)
            print("Task added successfully.")
        elif command == "2":
            title = input("Enter task title to remove: ")
            self.task_manager.remove_task(title)
            print("Task removed successfully.")
        elif command == "3":
            print("Listing all tasks:")
            self.task_manager.list_tasks()
        elif command == "4":
            title = input("Enter task title to mark as complete: ")
            self.task_manager.mark_task_complete(title)
            print("Task marked as complete.")
        elif command == "5":
            title = input("Enter task title to mark as incomplete: ")
            self.task_manager.mark_task_incomplete(title)
            print("Task marked as incomplete.")
        elif command == "6":
            print("Command History:")
            for i, cmd in enumerate(self.command_history, 1):
                print(f"{i}. {cmd}")
        elif command == "7":
            self.change_theme()
        elif command == "8":
            print("Exiting Task Manager. Goodbye!")
        else:
            print("Invalid command. Please try again.")

    def change_theme(self):
        """
        Allows the user to change the console theme.
        """
        print("\nAvailable Themes:")
        print("1. Default")
        print("2. Dark Mode")
        print("3. Light Mode")
        choice = input("Choose a theme (1-3): ")

        if choice == "1":
            self.theme = "default"
            print("Theme set to Default.")
        elif choice == "2":
            self.theme = "dark"
            print("Theme set to Dark Mode.")
        elif choice == "3":
            self.theme = "light"
            print("Theme set to Light Mode.")
        else:
            print("Invalid choice. Theme not changed.")

    def run(self):
        """
        Runs the console interface, displaying the menu and processing user input.
        """
        while True:
            self.display_menu()
            command = input("Enter your choice: ")
            if command == "8":  # Exit command
                break
            self.execute_command(command)




