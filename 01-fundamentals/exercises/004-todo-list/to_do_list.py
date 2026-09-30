
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
        user_option = int(input("Enter a option: "))
        if user_option not in range(1,6):
            print("You have to enter a valid option.")
            continue 
        match user_option:
            case 1: 
                print("Add task")
            case 2:
                print("Complete task")
            case 3:
                print("Delete task")
            case 4:
                print("Show task")
            case 5:
                print("Quit")
                break
        
    except ValueError: 
        print("Invalid option.")

    
""" 
while True: 
    user_input = input("Enter a task: ")
    if  user_input == 'q':
        break
    task = {}
    task["title"] = user_input 
    task["completed"] = False
    user_tasks.append(task)

print("Your tasks:")
show_tasks(user_tasks)

select_task = int(input("Enter the task number to complete: "))
task_index = select_task - 1
user_tasks[task_index]['completed'] = True
show_tasks(user_tasks)

pop_task = int(input("Enter the task number to delete: "))

pop_index = pop_task - 1
user_tasks.pop(pop_index)

print("Your Current Tasks:")
show_tasks(user_tasks)
"""
