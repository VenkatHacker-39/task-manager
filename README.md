Project Title: **Task Manager CLI Application**

Objective: Build a command-line interface (CLI) application to manage tasks. The application should allow users to add, view, and delete tasks, as well as save and load tasks from a file.

STEP - 1

-> Creating project directory named task_manager
-> Inside the directory, creating a Python file named task_manager.py

STEP - 2

-> In task_manager.py import Json libary
-> **Project Structure**

The project is organized as follows:

-> Task Class: Represents a single task with attributes:
-> task_id: Unique integer identifier for the task.
-> task_name: A short description or title for the task.
-> is_done: Boolean indicating whether the task is complete.

STEP - 3

-> **Features**

-> Add Task: Allows users to add a new task to the list. Each task is assigned a unique ID for easy reference.
-> View All Tasks: Displays all tasks in the list, showing each task’s ID, title, and completion status.
-> Delete Task: Remove a task by entering its unique ID.
-> Mark Task as Completed: Update the completion status of a specific task.
-> Save Tasks: Save the current list of tasks to a JSON file (tasks.json) to preserve tasks between sessions.
-> Load Tasks: Automatically loads tasks from tasks.json on startup, restoring the task list from the previous session if the file exists.

STEP - 4

-> **TaskManager Class**: Manages a list of tasks and provides methods to:
  - Add new tasks.
  - Delete tasks by ID.
  - Mark tasks as completed.
  - Save and load tasks to/from a JSON file.
  - Automatically assign a unique ID to each new task.
  - Exit
  
-> **main() Function**: The main entry point providing a menu-driven interface for user interaction.

