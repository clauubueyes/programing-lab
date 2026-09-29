
user_task = []
user_input1 = input("Enter a task: ")
user_input2 = input("Enter a task: ")
user_input3 = input("Enter a task: ")

user_task.append(user_input1)
user_task.append(user_input2)
user_task.append(user_input3)

print("Your tasks:")

for task in user_task: 
    print(task)