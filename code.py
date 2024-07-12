# Dictionary to store tasks with their details
todo_list = {}

# Function to add a task to the to-do list
def add_task():
    task_name = input("Enter task name: ")
    task_description = input("Enter task description: ")
    task_due_date = input("Enter due date (optional, press Enter to skip): ").strip()

    task_details = {
        'name': task_name,
        'description': task_description,
        'due_date': task_due_date if task_due_date else 'No due date'
    }

    todo_list[len(todo_list) + 1] = task_details
    print("Task added!\n")

# Function to delete a task from the to-do list
def delete_task():
    task_number = int(input("Enter task number to delete: "))
    if task_number in todo_list:
        del todo_list[task_number]
        print("Task deleted!\n")
    else:
        print("Task number not found!\n")

# Function to view all tasks in the to-do list
def view_tasks():
    if not todo_list:
        print("No tasks in the to-do list.\n")
    else:
        print("To-Do List:")
        for num, task_details in todo_list.items():
            print(f"Task {num}:")
            print(f"  Name: {task_details['name']}")
            print(f"  Description: {task_details['description']}")
            print(f"  Due Date: {task_details['due_date']}")
            print()
        print()

# Main program loop
while True:
    print("To-Do List Menu:")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Mark Task as Completed")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        delete_task()
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        print("Feature not implemented yet.\n")  # Placeholder for marking task as completed
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.\n")
