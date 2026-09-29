"""
user_task = []

print("Enter 'q' to quit")

while True: 
    user_input = input("Enter a task: ")
    
    if  user_input == 'q':
        break
    user_task.append(user_input)

print("Your tasks:")

for task in user_task: 
    print(task)

"""

tasks = []

task1 = {}
task2 = {}

task1["title"] = "Learn JS"
task1["completed"] = False 

task2["title"] = "Practice CSS"
task2["completed"] = False 

tasks.append(task1)
tasks.append(task2)

for task in tasks:
    print(f"Title: {task['title']}")
#print(f"\nTask: {task['title']}\nCompleted: {task['completed']}\n")
    