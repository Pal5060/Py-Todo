from tasks import load_tasks, add_task, delete_task_by_id, mark_task_done_by_id


def print_tasks(show_ids=False):
    tasks = load_tasks()
    if not tasks:
        print("No tasks found. Add one!")
        return []
    print('\nTasks:')
    for i, t in enumerate(tasks):
        mark = '✔' if t.get('done') else ' '
        task_id_display = f" (ID: {t.get('id')})" if show_ids else ""
        print(f"{i+1}. [{mark}] {t.get('name')}{task_id_display}")
    return tasks


def main():
    while True:
        print('\n=== To-Do Manager (CLI) ===')
        print('1) Add Task')
        print('2) View Tasks')
        print('3) Mark Task as Done')
        print('4) Delete Task')
     

        if choice == '1':
            name = input('Task name: ').strip()
            if name:
                due_date = input('Due date (YYYY-MM-DD, optional): ').strip() or None
                due_time = input('Due time (HH:MM, optional): ').strip() or None
                priority = input('Priority (High, Medium, Low, default Low): ').strip() or 'Low'
                
                add_task(name, due_date=due_date, due_time=due_time, priority=priority)
                print('Task added.')
            else:
                print('Empty task not added.')
        elif choice == '2':
            print_tasks(show_ids=False) # Don't show IDs by default for simplicity
        elif choice == '3':
            current_tasks = print_tasks() # Get tasks to map index to ID
            idx = input('Task number to mark done: ').strip()
            if idx.isdigit():
                task_index = int(idx) - 1
                if 0 <= task_index < len(current_tasks):
                    if mark_task_done_by_id(current_tasks[task_index]['id']):
                        print('Task marked done.')
                    else:
                        print('Failed to mark task done.')
                else:
                    print('Invalid task number.')
            else:
                print('Please enter a number.')
        elif choice == '4':
            current_tasks = print_tasks() # Get tasks to map index to ID
            idx = input('Task number to delete: ').strip()
            if idx.isdigit():
                task_index = int(idx) - 1
                if 0 <= task_index < len(current_tasks):
                    if delete_task_by_id(current_tasks[task_index]['id']):
                        print('Task deleted.')
                    else:
                        print('Failed to delete task.')
                else:
                    print('Invalid task number.')
            else:
                print('Please enter a number.')
        elif choice == '5':
            print('Goodbye!')
            break
        else:
            print('Invalid option, try again.')


if __name__ == '__main__':
    main()
