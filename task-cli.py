#https://roadmap.sh/projects/task-tracker
import sys
import argparse

parser = argparse.ArgumentParser(description="Testing argparse")
subparsers = parser.add_subparsers(dest="command", help="Avaliable commands")

add_parser = subparsers.add_parser("add", help="Add a task")
add_parser.add_argument("name", type=str, help="The name of the task")

update_parser = subparsers.add_parser("update", help="Update a task")
update_parser.add_argument("name", type=str, help="Name of task you want to update")

delete_parser = subparsers.add_parser("delete", help="Delete a task")
delete_parser.add_argument("name", type=str, help="Name of the task you want to delete")

parser.add_argument("-v", "--verbose", action="store_true", help="Activate verbose mode")

args = parser.parse_args()

if args.command == "add":
    print(f"added a task, {args.name}")
if args.command == "update":
    print(f"updated a task, {args.name}")
if args.command == "delete":
    print(f"deletet a task, {args.name}")