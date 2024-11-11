import json

class Task:
    def __init__(self, task_id, task_name, is_done=False):
        self.task_id = task_id
        self.task_name = task_name
        self.is_done = is_done
#Marks the task as completed

    def mark_as_done(self):
        self.is_done = True
#Convert task to a dictionary for JSON serialization

    def to_dict(self):
        return {"id": self.task_id, "title": self.task_name, "completed": self.is_done}

#Create a Task instance from a dictionary
    @classmethod
    def from_dict(cls, task_data):
        return cls(task_data["id"], task_data["title"], task_data["completed"])


    def __str__(self):
        status = "Completed" if self.is_done else "Incomplete"
        return f"Task {self.task_id}: {self.task_name} [{status}]"


class TaskList:
    def __init__(self, storage_file="tasks.json"):
        self.storage_file = storage_file
        self.all_tasks = []
        self.load_tasks()
        self.next_task_id = self.get_next_task_id()

#Get the next ID incrementally based on the current list length
    def get_next_task_id(self):
        return len(self.all_tasks) + 1

#Add a new task to the task list
    def add_new_task(self, task_name):
        new_task = Task(task_id=self.next_task_id, task_name=task_name)
        self.all_tasks.append(new_task)
        self.next_task_id += 1
        print(f"Task '{task_name}' added with ID {new_task.task_id}.")

#Display all tasks
    def display_tasks(self):
        if not self.all_tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for task in self.all_tasks:
                print(task)

#Delete a task by its ID
    def remove_task(self, task_id):
        task_found = False
        self.all_tasks = [task for task in self.all_tasks if not (task_found := task.task_id == task_id)]
        if task_found:
            print(f"Task with ID {task_id} deleted.")
        else:
            print("Task not found.")

#Mark a task as completed
    def complete_task(self, task_id):
        for task in self.all_tasks:
            if task.task_id == task_id:
                task.mark_as_done()
                print(f"Task '{task.task_name}' marked as completed.")
                return
        print("Task not found.")

#Save tasks to a JSON file
    def save_tasks(self):
        with open(self.storage_file, 'w') as file:
            json.dump([task.to_dict() for task in self.all_tasks], file, indent=4)
        print("Tasks saved to tasks.json.")

#Load tasks from a JSON file if it exists.
    def load_tasks(self):
        try:
            with open(self.storage_file, 'r') as file:
                self.all_tasks = [Task.from_dict(data) for data in json.load(file)]
        except FileNotFoundError:
            self.all_tasks = []

def main():
    task_list = TaskList()

    while True:
        print("\n" + "="*35)
        print("        Task Manager Menu        ")
        print("="*35)
        print(" [1] -> Add a New Task")
        print(" [2] -> View All Tasks")
        print(" [3] -> Delete a Task")
        print(" [4] -> Mark Task as Completed")
        print(" [5] -> Save Tasks to File")
        print(" [6] -> Exit Application")
        print("="*35)

        choice = input("Choose an option: ")

        if choice == "1":
            task_name = input("Enter the task title: ")
            task_list.add_new_task(task_name)
        elif choice == "2":
            task_list.display_tasks()
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to delete: "))
                task_list.remove_task(task_id)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                task_list.complete_task(task_id)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            task_list.save_tasks()
        elif choice == "6":
            task_list.save_tasks()  # Save before exiting
            print("Exiting the Task Manager.")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
