# Task-Manager
---
Task Manager is a simple command-line Python script that allows you to manage your tasks. You can add tasks, view your task list, and delete tasks you've completed. It's a straightforward tool designed for personal task tracking.
## Features
- **Add Task**: Easily add tasks to your task list.
- **View Tasks**: View your current task list, along with task numbers.
- **Delete Task**: Remove completed tasks by specifying their task number.
## How to Use
1. Clone this repository to your local machine.
   ```shell
   git clone https://github.com/your-username/task-manager.git
   ```
Make sure to replace `"your-username"` with your actual GitHub username in the clone command, and adjust any other details as needed.
2. Navigate to the project directory.
   ```shell
   cd task-manager
   ```
3. Run the script.
   ```shell
   python task_manager.py
   ```
4. Use the menu options to add, view, or delete tasks.
5. Follow the on-screen prompts to interact with the task manager.
## Usage
- **Add a Task**: Choose option `1`, then enter the task description when prompted.
- **View Tasks**: Choose option `2` to see your current task list.
- **Delete Task**: Choose option `3`, follow the on-screen instructions to select a task to delete.
- **Exit**: Choose option `4` to exit the task manager.
## Contributing
Feel free to contribute to this project by opening issues or submitting pull requests. Your input and suggestions are welcome!
---
Let's Start Coding

tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def delete_task():
    view_tasks()
    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to delete: "))
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f"Deleted task: {deleted_task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def print_menu():
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    print_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Exiting Task Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-4).")
