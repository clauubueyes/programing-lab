
user_task = []

for i in range(3):
    user_input = input("Enter a task: ")
    user_task.append(user_input)

print("Your tasks:")

for task in user_task: 
    print(task)