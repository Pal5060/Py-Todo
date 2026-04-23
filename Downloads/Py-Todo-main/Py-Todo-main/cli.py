from tasks import load_tasks, add_task, delete_task, mark_done


def print_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found. Add one!")
        return
    print('\nTasks:')
    for i, t in enumerate(tasks):
        mark = '✔' if t.get('done') else ' '
        print(f"{i+1}. [{mark}] {t.get('name')}")


def main():
    while True:
        print('\n=== To-Do Manager (CLI) ===')
        print('1) Add Task')
        print('2) View Tasks')
        print('3) Mark Task as Done')
        print('4) Delete Task')
        print('5) Exit')
        choice = input('Choose an option: ').strip()

        if choice == '1':
            name = input('Task name: ').strip()
            if name:
                add_task(name)
                print('Task added.')
            else:
                print('Empty task not added.')
        elif choice == '2':
            print_tasks()
        elif choice == '3':
            print_tasks()
            idx = input('Task number to mark done: ').strip()
            if idx.isdigit():
                if mark_done(int(idx)-1):
                    print('Task marked done.')
                else:
                    print('Invalid task number.')
            else:
                print('Please enter a number.')
        elif choice == '4':
            print_tasks()
            idx = input('Task number to delete: ').strip()
            if idx.isdigit():
                if delete_task(int(idx)-1):
                    print('Task deleted.')
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
