
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
