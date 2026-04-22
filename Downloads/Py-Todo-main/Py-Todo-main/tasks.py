import json
import os
import tempfile

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')


def load_tasks():
    """Load tasks from the JSON file. Returns a list of task dicts."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_tasks(tasks):
    """Save the list of tasks to the JSON file using an atomic write."""
    dirn = os.path.dirname(DATA_FILE)
    fd, tmp_path = tempfile.mkstemp(dir=dirn)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, indent=2, ensure_ascii=False)
        os.replace(tmp_path, DATA_FILE)
    except Exception as e:
        print(f"Error saving tasks: {e}")
        # If anything fails, try to clean up the temp file
        try:
            os.remove(tmp_path)
        except OSError:
            pass


def add_task(name):
    tasks = load_tasks()
    tasks.append({"name": name, "done": False})
    save_tasks(tasks)


def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
        return True
    return False


def mark_done(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        return True
    return False


def clear_all():
    save_tasks([])
