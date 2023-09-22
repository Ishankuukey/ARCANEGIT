todo_list = []


def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")


def view_tasks():
    if not todo_list:
        print("The to-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")


def remove_task(task_index):
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the to-do list.")
    else:
        print("Invalid task index.")


while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        task = input("Enter a task to add: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        task_index = int(
            input("Enter the index of the task to remove (0 to cancel): "))
        if task_index != 0:
            remove_task(task_index)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
