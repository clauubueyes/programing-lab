
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