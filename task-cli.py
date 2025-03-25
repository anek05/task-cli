#https://roadmap.sh/projects/task-tracker
import sys
import argparse
import json
from task import Task

# Try to read tasks from tasks.json file
try:
    with open("tasks.json", "r") as file:
        # Read file content and parse JSON, defaulting to empty list if file is empty
        content = file.read()
        task_list = json.loads(content) if content else []
except (FileNotFoundError, json.JSONDecodeError):
    # If file doesn't exist or has invalid JSON, start with empty task list
    task_list = []


#argument parser setup
parser = argparse.ArgumentParser(description="Testing argparse")
subparsers = parser.add_subparsers(dest="command", help="Avaliable commands")

add_parser = subparsers.add_parser("add", help="Add a task")
add_parser.add_argument("description", type=str, help="The description of the task")

update_parser = subparsers.add_parser("update", help="Update a task")
update_parser.add_argument("id", type=int, help="ID of the task you want to update")
update_parser.add_argument("description", type=str, help="The description of the task")

delete_parser = subparsers.add_parser("delete", help="Delete a task")
delete_parser.add_argument("id", type=int, help="ID of the task you want to delete")

parser.add_argument("-v", "--verbose", action="store_true", help="Activate verbose mode")
args = parser.parse_args()
#############################################################################################

if args.command == "add":
    #Find the highest id of the tasks
    highest_id = max(task["id"] for task in task_list) if task_list else 0
    new_task = Task(highest_id+1, args.description)
    # Convert Task object to dictionary before adding to list
    task_dict = {
        "id": new_task.id,
        "description": new_task.description,
        "status": new_task.status,
        "createdAt": new_task.createdAt.isoformat(),
        "updatedAt": new_task.updatedAt.isoformat()
    }
    task_list.append(task_dict)
    with open("tasks.json", "w") as file:
        json.dump(task_list, file, indent=4)
    print(f"Added task: {new_task.description}")

if args.command == "update":
    task_list[args.id-1]["description"] = args.description
    with open("tasks.json", "w") as file:
        json.dump(task_list, file, indent=4)
    print(f"updated a task, {args.description}")

if args.command == "delete":
    task_to_delete = task_list[args.id-1]
    task_list.pop(args.id-1)
    with open("tasks.json", "w") as file:
        json.dump(task_list, file, indent=4)
    print(f"deleted a task, {task_to_delete['description']}")

