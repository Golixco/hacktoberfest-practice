# todo.py
# Author: Rohan Sonu Bablani (Golixco)
# Simple CLI todo app that stores tasks in tasks.json
# Basic features: add, list, done, remove, clear

import json
import argparse
from pathlib import Path
from datetime import datetime

DATA_FILE = Path("tasks.json")

def load_tasks():
    if not DATA_FILE.exists():
        return []
    try:
        return json.loads(DATA_FILE.read_text())
    except Exception:
        return []

def save_tasks(tasks):
    DATA_FILE.write_text(json.dumps(tasks, indent=2))

def add_task(text):
    tasks = load_tasks()
    tasks.append({
        "id": int(datetime.now().timestamp()),
        "text": text,
        "done": False,
        "created": datetime.now().isoformat()
    })
    save_tasks(tasks)
    print("Added:", text)

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks. Add one with `todo.py add \"Buy milk\"`.")
        return
    for i, t in enumerate(tasks, 1):
        status = "✓" if t.get("done") else " "
        print(f"{i}. [{status}] {t.get('text')} (id:{t.get('id')})")

def mark_done(index):
    tasks = load_tasks()
    if index < 1 or index > len(tasks):
        print("Invalid task number.")
        return
    tasks[index-1]["done"] = True
    save_tasks(tasks)
    print("Marked done:", tasks[index-1]["text"])

def remove_task(index):
    tasks = load_tasks()
    if index < 1 or index > len(tasks):
        print("Invalid task number.")
        return
    removed = tasks.pop(index-1)
    save_tasks(tasks)
    print("Removed:", removed["text"])

def clear_tasks():
    save_tasks([])
    print("All tasks cleared.")

def parse_args():
    p = argparse.ArgumentParser(prog="todo.py", description="Simple CLI todo app")
    sp = p.add_subparsers(dest="cmd")
    sp_add = sp.add_parser("add")
    sp_add.add_argument("text", nargs="+", help="Task text")
    sp_list = sp.add_parser("list")
    sp_done = sp.add_parser("done")
    sp_done.add_argument("number", type=int, help="Task number from list")
    sp_rm = sp.add_parser("remove")
    sp_rm.add_argument("number", type=int, help="Task number from list")
    sp_clear = sp.add_parser("clear")
    return p.parse_args()

def main():
    args = parse_args()
    if args.cmd == "add":
        add_task(" ".join(args.text))
    elif args.cmd == "list" or args.cmd is None:
        list_tasks()
    elif args.cmd == "done":
        mark_done(args.number)
    elif args.cmd == "remove":
        remove_task(args.number)
    elif args.cmd == "clear":
        clear_tasks()
    else:
        print("Unknown command. Use add/list/done/remove/clear")

if __name__ == "__main__":
    main()
