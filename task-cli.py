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

list_parser = subparsers.add_parser("list", help="List all tasks")
list_parser.add_argument("-a", "--all", action="store_true", help="Show all tasks")
list_parser.add_argument("-t", "--todo", action="store_true", help="Show todo tasks")
list_parser.add_argument("-i", "--in-progress", action="store_true", help="Show in progress tasks")
list_parser.add_argument("-d", "--done", action="store_true", help="Show done tasks")

todo_parser = subparsers.add_parser("mark-todo", help="Change task status to todo")
todo_parser.add_argument("id", type=int, help="ID of the task you want to change to todo")

in_progress_parser = subparsers.add_parser("mark-in-progress", help="Change task status to in progress")
in_progress_parser.add_argument("id", type=int, help="ID of the task you want to change to in progress")

done_parser = subparsers.add_parser("mark-done", help="Change task status to done")
done_parser.add_argument("id", type=int, help="ID of the task you want to change to done")

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

if args.command == "list":
    if args.all:
        for task in task_list:
            print(task)
    elif args.todo:
        for task in task_list:
            if task["status"] == "todo":
                print(task)
    elif args.in_progress:
        for task in task_list:
            if task["status"] == "in progress":
                print(task)
    elif args.done:
        for task in task_list:
            if task["status"] == "done":
                print(task)

if args.command == "mark-todo":
    task_list[args.id-1]["status"] = "todo"
    with open("tasks.json", "w") as file:
        json.dump(task_list, file, indent=4)
    print(f"Changed task {args.id} to todo")
    
if args.command == "mark-in-progress":
    task_list[args.id-1]["status"] = "in progress"
    with open("tasks.json", "w") as file:
        json.dump(task_list, file, indent=4)
    print(f"Changed task {args.id} to in progress")
    
if args.command == "mark-done":
    task_list[args.id-1]["status"] = "done"
    with open("tasks.json", "w") as file:
        json.dump(task_list, file, indent=4)
    print(f"Changed task {args.id} to done")
    
