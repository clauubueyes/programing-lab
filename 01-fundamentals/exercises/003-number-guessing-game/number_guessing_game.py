import random

machine_number = random.randint(1,100)

count = 0
while count < 5:
    user_number = int(input("Enter an integer number: "))
    count += 1
    if user_number < machine_number: 
        print("Too Low!")  
    elif user_number > machine_number: 
        print("Too High!")
    else: 
        print("You win!")
        break
    print(f"You have {5 - count} attempts ")
else: 
    print(f"You lose! The number was {machine_number}")