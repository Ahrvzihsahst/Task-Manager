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
