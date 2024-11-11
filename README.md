# task-cli

## Table of Contents
- [Task Tracker](#task-tracker)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Features](#features)

## Task Tracker

A simple [command-line application](https://roadmap.sh/projects/task-tracker) to track tasks and manage a to-do list, developed as part of [roadmap.sh](https://roadmap.sh/) projects.


## Getting Started
Clone the repository

    git clone https://github.com/KerlyLaeda/task-cli.git
Navigate to project directory

    cd task-cli
Run the application

    task-cli <command> <params>

## Prerequisites
- [Python 3.x](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

## Usage
### Adding a New Task
Add a task by specifying the description:
    
    task-cli add <description>
    # Output: Task added successfully (ID: 1)

### Updating and Deleting Tasks
Update or delete tasks by specifying the task ID:

    task-cli update <task-id> <updated_description>
    task-cli delete <task-id>

### Changing Task Status
Mark a task as in progress, done, or reset to todo:

    task-cli mark-in-progress <task-id>
    task-cli mark-done <task-id>
    task-cli mark-todo <task-id>

### Listing Tasks
List all tasks or filter by status:

    task-cli list
    task-cli list done
    task-cli list todo
    task-cli list in-progress

## Features
- **Add, Update, and Delete Tasks**: Easily manage your tasks.
- **Change Task Status**: Mark tasks as in progress, done, or revert them to todo.
- **Filter Tasks by Status**: View tasks by their current status to stay organized.
- **Persistent Storage**: Tasks are saved in a JSON file for persistence across sessions.
