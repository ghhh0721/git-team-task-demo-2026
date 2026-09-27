"""A tiny command-line task list stored in a JSON file."""

import argparse
import json
from pathlib import Path


DATA_FILE = Path("tasks.json")


def load_tasks():
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_tasks(tasks):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)


def main():
    parser = argparse.ArgumentParser(description="简单的待办清单")
    commands = parser.add_subparsers(dest="command", required=True)
    add_command = commands.add_parser("add", help="添加任务")
    add_command.add_argument("text", help="任务内容")
    commands.add_parser("list", help="查看任务")
    done_command = commands.add_parser("done", help="完成任务")
    done_command.add_argument("number", type=int, help="任务编号")
    args = parser.parse_args()

    tasks = load_tasks()
    if args.command == "add":
        tasks.append({"text": args.text, "done": False})
        save_tasks(tasks)
        print("已添加任务")
    elif args.command == "done":
        tasks[args.number - 1]["done"] = True
        save_tasks(tasks)
        print("任务已完成")
    elif not tasks:
        print("暂无任务")
    else:
        for number, task in enumerate(tasks, start=1):
            mark = "x" if task["done"] else " "
            print(f"{number}. [{mark}] {task['text']}")


if __name__ == "__main__":
    main()
