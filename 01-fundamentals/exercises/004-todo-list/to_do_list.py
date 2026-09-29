
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

for index, task in enumerate(user_tasks, start= 1): 
    print(f"\t{index}. [] {task['title']}")

select_task = int(input("Enter the task number to complete: "))
task_index = select_task - 1
user_tasks[task_index]['completed'] = True

for index, task in enumerate(user_tasks, start= 1):
    if task['completed'] == True:
        print(f"\t{index}. [x] {task['title']}")
    elif task['completed'] == False:
        print(f"\t{index}. [] {task['title']}")

