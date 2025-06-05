import json
import os
import argparse
from typing import List, Dict

TASKS_FILE = 'tasks.json'

def load_tasks() -> List[Dict]:
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_tasks(tasks: List[Dict]):
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=2)

def add_task(description: str, note: str = ''):
    tasks = load_tasks()
    task_id = max([t['id'] for t in tasks], default=0) + 1
    tasks.append({'id': task_id, 'description': description, 'note': note, 'done': False})
    save_tasks(tasks)
    print(f'Task {task_id} added.')

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print('No tasks found.')
        return
    for t in tasks:
        status = '✓' if t['done'] else ' '
        note = f" - {t['note']}" if t['note'] else ''
        print(f"[{status}] {t['id']}: {t['description']}{note}")

def add_note(task_id: int, note: str):
    tasks = load_tasks()
    for t in tasks:
        if t['id'] == task_id:
            t['note'] = note
            save_tasks(tasks)
            print(f'Note added to task {task_id}.')
            return
    print(f'Task {task_id} not found.')

def mark_done(task_id: int):
    tasks = load_tasks()
    for t in tasks:
        if t['id'] == task_id:
            t['done'] = True
            save_tasks(tasks)
            print(f'Task {task_id} marked as done.')
            return
    print(f'Task {task_id} not found.')

def remove_task(task_id: int):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t['id'] != task_id]
    if len(new_tasks) == len(tasks):
        print(f'Task {task_id} not found.')
        return
    save_tasks(new_tasks)
    print(f'Task {task_id} removed.')

def main():
    parser = argparse.ArgumentParser(description='Task Noting Program')
    subparsers = parser.add_subparsers(dest='command', required=True)

    add_p = subparsers.add_parser('add', help='Add a new task')
    add_p.add_argument('description', help='Task description')
    add_p.add_argument('--note', help='Optional note', default='')

    list_p = subparsers.add_parser('list', help='List tasks')

    note_p = subparsers.add_parser('note', help='Add note to task')
    note_p.add_argument('id', type=int, help='Task ID')
    note_p.add_argument('note', help='Note text')

    done_p = subparsers.add_parser('done', help='Mark task as done')
    done_p.add_argument('id', type=int, help='Task ID')

    remove_p = subparsers.add_parser('remove', help='Remove a task')
    remove_p.add_argument('id', type=int, help='Task ID')

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.description, args.note)
    elif args.command == 'list':
        list_tasks()
    elif args.command == 'note':
        add_note(args.id, args.note)
    elif args.command == 'done':
        mark_done(args.id)
    elif args.command == 'remove':
        remove_task(args.id)

if __name__ == '__main__':
    main()
