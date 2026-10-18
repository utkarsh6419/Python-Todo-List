"""A tiny persistent command-line to-do list."""

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    return json.loads(DATA_FILE.read_text()) if DATA_FILE.exists() else []


def save_tasks(tasks):
    DATA_FILE.write_text(json.dumps(tasks, indent=2))


def main():
    tasks = load_tasks()
    while True:
        print("\n1) View  2) Add  3) Complete  4) Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            if not tasks:
                print("No tasks yet.")
            for number, task in enumerate(tasks, 1):
                mark = "x" if task["done"] else " "
                print(f"{number}. [{mark}] {task['title']}")
        elif choice == "2":
            title = input("Task: ").strip()
            if title:
                tasks.append({"title": title, "done": False})
                save_tasks(tasks)
        elif choice == "3":
            try:
                tasks[int(input("Task number: ")) - 1]["done"] = True
                save_tasks(tasks)
            except (ValueError, IndexError):
                print("Invalid task number.")
        elif choice == "4":
            return
        else:
            print("Choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
