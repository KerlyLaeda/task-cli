#!/usr/bin/env python3
import argparse
import json
from _datetime import datetime


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


def prettify_output(tasks):
    max_key_length = max(len(key) for task in tasks for key in task.keys())

    for task in tasks:
        for key, value in task.items():
            print(f"  {key.ljust(max_key_length)}\t{value}")
        print()


def add(description):
    tasks = load_file()
    task_id = len(tasks) + 1
    created_at = datetime.now().strftime("%d/%m/%Y, %H:%M")

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
            task["updatedAt"] = datetime.now().strftime("%d/%m/%Y, %H:%M")
            save_file(tasks)
            print(f"Task {task_id} was updated successfully.")
            return
    print(f"Task with ID {task_id} not found.")


def delete(task_id):
    tasks = load_file()
    tasks = [task for task in tasks if task_id != task["id"]]
    save_file(tasks)
    print(f"Task {task_id} was deleted successfully")


def toggle_status(task_id, status):
    tasks = load_file()
    for task in tasks:
        if task_id == task["id"]:
            if status == "mark-in-progress":
                task["status"] = "in-progress"
            elif status == "mark-done":
                task["status"] = "done"
            # In case the user wants to revert changes or status not recognizable
            else:
                task["status"] = "todo"

            task["updatedAt"] = datetime.now().strftime("%d/%m/%Y, %H:%M")
            print(f"Task {task_id} status changed to {task['status']}.")
            break

    save_file(tasks)


def list_tasks(status=None):
    tasks = load_file()

    if not tasks:
        print("There are no tasks yet. Want to add a new task? (y/n)")
        choice = input().lower()
        if choice == "y":
            description = input("Enter a task description: ")
            add(description)
        elif choice == "n":
            pass
        else:
            print("Invalid input")
        return

    if status:
        filtered_tasks = [task for task in tasks if task["status"] == status]
        if not filtered_tasks:
            print(f"No tasks with the status {status}.")
            return

        tasks = filtered_tasks

    for task in tasks:
        prettify_output([task])


def main():
    parser = argparse.ArgumentParser(prog="task-cli")
    parser.add_argument("command", choices=[
        "add",
        "update",
        "delete",
        "list",
        "list todo",
        "list in-progress",
        "list done",
        "mark-in-progress",
        "mark-done",
        "mark-todo"])
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

    elif args.command == "delete":
        if len(args.params) < 1:
            print("Error: 'delete' requires an ID of task to delete.")
        else:
            try:
                task_id = int(args.params[0])
                delete(task_id)
            except ValueError:
                print("Invalid ID.")

    elif args.command in ["mark-in-progress", "mark-done", "mark-todo"]:
        if len(args.params) < 1:
            print("Error: changing status requires task ID.")
        else:
            try:
                task_id = int(args.params[0])
                toggle_status(task_id, args.command)
            except ValueError:
                print("Invalid ID.")

    elif args.command in ["list", "list todo", "list in-progress", "list done"]:
        status = args.params[0] if args.params else None
        list_tasks(status)


if __name__ == "__main__":
    main()
