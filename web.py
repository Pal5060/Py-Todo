from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime
import uuid
from tasks import load_tasks, save_tasks, mark_task_done_by_id, delete_task_by_id

app = Flask(__name__, static_folder='static', template_folder='templates')

def make_task_id():
    return uuid.uuid4().hex


def task_overdue(task):
    if task.get('done'):
        return False
    date = task.get('due_date')
    time = task.get('due_time')
    if not date:
        return False
    dt_str = f"{date} {time or '00:00'}"
    try:
        dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M')
        return dt < datetime.now().replace(second=0, microsecond=0) # Compare without seconds/microseconds
    except ValueError: # Catch specific error for strptime
        return False


@app.route('/', methods=['GET'])
def index():
    # Define a mapping for priority to numerical value for correct sorting
    priority_map = {
        'High': 3,
        'Medium': 2,
        'Low': 1
    }

    tasks = load_tasks()
    # compute derived fields
    for t in tasks:
        t['overdue'] = task_overdue(t)
    # sort: not done first, overdue high priority
    tasks = sorted(tasks, key=lambda x: (
        x.get('done'), # False (not done) comes before True (done)
        x.get('overdue') is False, # False (overdue) comes before True (not overdue)
        -priority_map.get(x.get('priority', 'Low'), 0) # Higher number (priority) comes first
    ))
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name', '').strip()
    due_date = request.form.get('due_date', '').strip() or None
    due_time = request.form.get('due_time', '').strip() or None
    priority = request.form.get('priority', 'Low')

    if not name:
        return redirect(url_for('index'))
    tasks = load_tasks()
    task = {
        'id': make_task_id(),
        'name': name,
        'due_date': due_date,
        'due_time': due_time,
        'priority': priority,
        'done': False,
        'created_at': datetime.now().isoformat()
    }
    tasks.append(task) # Use the updated add_task if it were to be used directly here
    save_tasks(tasks)
    # support AJAX
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({'ok': True, 'task': task})
    return redirect(url_for('index'))


@app.route('/done/<task_id>', methods=['POST'])
def done(task_id):
    found = mark_task_done_by_id(task_id)
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({'ok': found})
    return redirect(url_for('index'))


@app.route('/delete/<task_id>', methods=['POST'])
def delete(task_id):
    deleted = delete_task_by_id(task_id)
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({'ok': deleted})
    return redirect(url_for('index'))


if __name__ == '__main__':
    # development server; for production use a WSGI server
    app.run(host='0.0.0.0', port=5000, debug=True)
