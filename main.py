# https://roadmap.sh/projects/task-tracker
import argparse
import json
import sys
import time


TASKS_FILE = "tasks.json"


def load_file():
    try:
        with open(TASKS_FILE) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_file(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add(description):
    tasks = load_file()
    task_id = len(tasks) + 1
    created_at = time.time()

    new_task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": created_at,
        "updatedAt": None,
    }

    tasks.append(new_task)
    save_file(tasks)
    print(f"Task added successfully (ID: {task_id})")


def update(task_id, new_description):
    tasks = load_file()
    for task in tasks:
        if task_id == task["id"]:
            task["description"] = new_description
            task["updatedAt"] = time.time()
            save_file(tasks)
            print(f"Task {task_id} was updated successfully.")
            return
    print(f"Task with ID {task_id} not found.")


def delete(task_id):
    tasks = load_file()

    save_file(tasks)
    print(f"Task {task_id} was deleted successfully")


def toggle_status():
    pass


def list_tasks():
    with open("tasks.json") as f:
        tasks = json.load(f)  # it will be stored as a Python dictionary

    if not tasks:
        print("There are no tasks yet. Want to add a new task? (y/n)")
        choice = input().lower()
        if choice == "y":
            add()
        elif choice == "n":
            pass
        else:
            print("Invalid input")
    else:
        print(tasks)


def main():
    parser = argparse.ArgumentParser(prog="task-cli")
    parser.add_argument("command", choices=["add", "update"])
    parser.add_argument("params", nargs="*")

    args = parser.parse_args()

    if args.command == "add":
        if len(args.params) < 1:
            print("Error: 'add' requires task description.")
        else:
            description = " ".join(args.params)
            add(description)

    elif args.command == "update":
        if len(args.params) < 2:
            print("Error: 'update' requires an ID of task to update and a new description.")
        else:
            try:
                task_id = int(args.params[0])
                new_description = " ".join(args.params[1:])
                update(task_id, new_description)
            except ValueError:
                print("Invalid ID.")








if __name__ == "__main__":
    main()
