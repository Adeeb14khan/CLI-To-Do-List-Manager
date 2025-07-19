import json
import os

TODO_FILE = "todos.json"

def load_todos():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return json.load(f)

def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=4)

def show_menu():
    print("\n--- Simple CLI TODO Manager ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def view_tasks(todos):
    if not todos:
        print("No tasks found.")
    else:
        for i, task in enumerate(todos, 1):
            print(f"{i}. {task}")

def add_task(todos):
    task = input("Enter new task: ").strip()
    if task:
        todos.append(task)
        save_todos(todos)
        print("Task added!")

def remove_task(todos):
    view_tasks(todos)
    try:
        idx = int(input("Enter task number to remove: "))
        if 1 <= idx <= len(todos):
            removed = todos.pop(idx - 1)
            save_todos(todos)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")

def main():
    todos = load_todos()
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            view_tasks(todos)
        elif choice == "2":
            add_task(todos)
        elif choice == "3":
            remove_task(todos)
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
