def add_task(title, tasks):
    task = {}
    task["title"] = title
    task["completed"] = False
    tasks.append(task)

def complete_task(select_index, tasks):
    index = select_index - 1
    tasks[index]['completed'] = True

def show_tasks(user_tasks):
    for index, task in enumerate(user_tasks, start=1):
        if task['completed']:
            print(f"\t{index}. [x] {task['title']}")
        else:
            print(f"\t{index}. [] {task['title']}")

user_tasks = []
print("------ TO-DO LIST ------\n")

print('''\t1. Add task
    \t2. Complete task
    \t3. Delete task
    \t4. Show tasks
    \t5. Quit\n''')

while True: 
    try:
        user_option = int(input("Enter an option: "))
        if user_option not in range(1,6):
            print("You have to enter a valid option.")
            continue 
        match user_option:
            case 1: 
                print("Add task")
                user_input = input("Enter a task: ")
                add_task(user_input, user_tasks)
                
            case 2:
                print("Complete task")
                if not user_tasks:
                    print("There are no tasks.")
                    continue
                show_tasks(user_tasks)
                select_task = int(input("Enter the task number to complete: "))
                if select_task not in range(1, len(user_tasks) + 1):
                    print("That task does not exist")
                    continue
                complete_task(select_task, user_tasks)
            case 3:
                print("Delete task")
                if not user_tasks:
                    print("There are no task")
                    continue
                show_tasks(user_tasks)
                pop_task = int(input("Enter the task number to delete: "))
                if pop_task not in range(1, len(user_tasks) + 1):
                    print("That task does not exist.")
                    continue
                pop_index = pop_task - 1
                user_tasks.pop(pop_index)
                
            case 4:
                print("Show tasks")
                print("Your tasks:")
                if not user_tasks:
                    print("There are no task.")
                    continue
                show_tasks(user_tasks)
            case 5:
                print("Quit")
                break
        
    except ValueError: 
        print("Invalid option.")
