from task_manager import *

def menu():
    print("\n--- TASK MANAGER ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")


def main():
    tasks = load_tasks()

    while True:
        menu()
        choice = input("Choose: ")

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            title = input("Task name: ")
            add_task(tasks, title)

        elif choice == "3":
            view_tasks(tasks)
            i = int(input("Task number: ")) - 1
            complete_task(tasks, i)

        elif choice == "4":
            view_tasks(tasks)
            i = int(input("Task number: ")) - 1
            delete_task(tasks, i)

        elif choice == "5":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
