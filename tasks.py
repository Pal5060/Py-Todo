import json
import os
import tempfile
import uuid # Import uuid for generating unique IDs
from datetime import datetime # Import datetime for created_at

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')


def load_tasks():
    """Load tasks from the JSON file. Returns a list of task dicts."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError, IOError) as e: # Catch FileNotFoundError explicitly
        return []


def save_tasks(tasks):
    """Save the list of tasks to the JSON file using an atomic write."""
    dirn = os.path.dirname(DATA_FILE)
    fd, tmp_path = tempfile.mkstemp(dir=dirn)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, indent=2, ensure_ascii=False)
        os.replace(tmp_path, DATA_FILE) # Atomic replacement
    except Exception as e:
        print(f"Error saving tasks: {e}")
        # If anything fails, try to clean up the temp file
        try:
            os.remove(tmp_path)
        except OSError:
            pass


def add_task(name, task_id=None, due_date=None, due_time=None, priority='Low', created_at=None):
    """
    Adds a new task to the list. Generates a unique ID if not provided.
    Supports additional fields for consistency with the web interface.
    """
    tasks = load_tasks()
    if task_id is None: # Ensure a unique ID is always generated if not explicitly provided
        task_id = uuid.uuid4().hex
    if created_at is None: # Ensure created_at is always set if not explicitly provided
        created_at = datetime.now().isoformat()
    task = {"id": task_id, "name": name, "done": False}
    if due_date: task['due_date'] = due_date # Keep original for now, but consider combined datetime object
    if due_time: task['due_time'] = due_time
    task['priority'] = priority
    task['likes'] = 0 # Initialize likes for new tasks
    task['created_at'] = created_at
    tasks.append(task)
    save_tasks(tasks)
    return task


def delete_task(index):
    tasks = load_tasks()
    # This function is now deprecated in favor of delete_task_by_id due to index unreliability.
    # For Tkinter/CLI, if index is still used, it means an internal list index, not a persistent ID.
    # It's better to update Tkinter/CLI to use task IDs.
    # For now, keeping it as is, but it should be replaced.
    print("Warning: delete_task(index) is deprecated. Use delete_task_by_id instead.")
    if 0 <= index < len(tasks) and 'id' in tasks[index]: # Check if task has an ID
        return delete_task_by_id(tasks[index]['id'])
    elif 0 <= index < len(tasks): # Fallback for tasks without IDs (older entries)
        tasks.pop(index)
        save_tasks(tasks)
        return True
    return False



def mark_done(index):
    tasks = load_tasks()
    # This function is now deprecated in favor of mark_task_done_by_id.
    print("Warning: mark_done(index) is deprecated. Use mark_task_done_by_id instead.")
    if 0 <= index < len(tasks) and 'id' in tasks[index]: # Check if task has an ID
        return mark_task_done_by_id(tasks[index]['id'])
    elif 0 <= index < len(tasks): # Fallback for tasks without IDs
        tasks[index]["done"] = True
        save_tasks(tasks)
        return True
    return False

def clear_all():
    save_tasks([])


def mark_task_done_by_id(task_id):
    """Mark a task as done by its ID. Returns True if found and updated."""
    tasks = load_tasks()
    found = False
    for task in tasks:
        if task.get('id') == task_id:
            task['done'] = True
            found = True
            break
    if found:
        save_tasks(tasks)
    return found


def delete_task_by_id(task_id):
    """Delete a task by its ID. Returns True if found and deleted."""
    tasks = load_tasks()
    initial_count = len(tasks)
    tasks_after_deletion = [t for t in tasks if t.get('id') != task_id]
    deleted = len(tasks_after_deletion) < initial_count
    if deleted:
        save_tasks(tasks_after_deletion)
    return deleted

def increment_task_likes_by_id(task_id):
    """Increment the likes count for a task by its ID. Returns the new like count or None if not found."""
    tasks = load_tasks()
    new_likes = None
    for task in tasks:
        if task.get('id') == task_id:
            task['likes'] = task.get('likes', 0) + 1 # Ensure 'likes' exists and increment
            new_likes = task['likes']
            break
    if new_likes is not None:
        save_tasks(tasks)
    return new_likes
