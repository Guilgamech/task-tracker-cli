# Task Manager Application

This is a command-line task manager that allows users to add, update, delete, and view tasks in different states (todo, in-progress, done). The tasks are stored in a `tasks.json` file. If the file does not exist, it will be created automatically.

## Requirements

- The application should be run from the command line.
- The user can interact with the application by passing arguments to perform various actions on tasks.
- The tasks are stored in the `tasks.json` file, which is located in the current directory.
- The user can add, update, delete tasks, and view tasks in different states (`todo`, `in-progress`, `done`).

## Features

- Add tasks
- Update tasks (change status to `todo`, `in-progress`, or `done`)
- Delete tasks
- List all tasks
- List tasks that are `done`
- List tasks that are `not done`
- List tasks that are `in-progress`

## Usage

### Add a task

```bash
python main.py add "Your task description here"
```

### Update a task

```bash
python main.py update <task_number> <status>
```

### Delete a task

```bash
python main.py delete <task_number>
```

### List a task

```bash
python main.py list
```

### List-Done a task

```bash
python main.py list-done
```

### List-Not-Done a task

```bash
python main.py list-not-done
```

### List-In-Progress a task

```bash
python main.py list-in-progress
```

## Project URL
-https://github.com/Guilgamech/task-tracker-cli
