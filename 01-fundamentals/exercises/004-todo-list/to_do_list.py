
def show_tasks(user_tasks):
    for index, task in enumerate(user_tasks, start=1):
        if task['completed'] == True:
            print(f"\t{index}. [x] {task['title']}")
        elif task['completed'] == False:
            print(f"\t{index}. [] {task['title']}")

user_tasks = []

print("Enter 'q' to quit")

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