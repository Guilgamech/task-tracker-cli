import json
import os
import sys
import uuid
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def list_tasks(filter_status=None):
    tasks = load_tasks()
    if filter_status:
        tasks = [task for task in tasks if task["status"] == filter_status]
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['description']} [{task['status']}] (Created: {task['createdAt']})")
    else:
        print("No tasks found.")

def add_task(description):
    tasks = load_tasks()
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_task = {
        "id": str(uuid.uuid4()),
        "description": description,
        "status": "todo",
        "createdAt": created_at,
        "updatedAt": created_at
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print("✅ Task added!")

def update_task(task_index, new_status):
    tasks = load_tasks()
    if 0 <= task_index - 1 < len(tasks):
        if new_status in ["todo", "in-progress", "done"]:
            tasks[task_index - 1]["status"] = new_status
            tasks[task_index - 1]["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            print("✅ Task updated!")
        else:
            print("❌ Invalid status. Use 'todo', 'in-progress', or 'done'.")
    else:
        print("❌ Invalid task number.")

def delete_task(task_index):
    tasks = load_tasks()
    if 0 <= task_index - 1 < len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        save_tasks(tasks)
        print(f"🗑️ Task deleted: {deleted_task['description']}")
    else:
        print("❌ Invalid task number.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <action> [arguments]")
        return
    
    action = sys.argv[1]
    
    if action == "list":
        list_tasks()
    elif action == "list-done":
        list_tasks("done")
    elif action == "list-not-done":
        list_tasks("todo")
    elif action == "list-in-progress":
        list_tasks("in-progress")
    elif action == "add" and len(sys.argv) > 2:
        add_task(" ".join(sys.argv[2:]))
    elif action == "update" and len(sys.argv) > 3:
        update_task(int(sys.argv[2]), sys.argv[3])
    elif action == "delete" and len(sys.argv) > 2:
        delete_task(int(sys.argv[2]))
    else:
        print("❌ Invalid command or missing arguments.")

if __name__ == "__main__":
    main()
