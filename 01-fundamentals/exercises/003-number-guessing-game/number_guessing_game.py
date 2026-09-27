import random

machine_number = random.randint(1,100)

count = 0
while count < 5:
    try: 
        user_number = int(input("Enter an integer number: "))
        if user_number  not in range(1,101):
            print("Enter a number between 1 and 100.")
            continue

        count += 1
        if user_number < machine_number: 
            print("Too Low!")  
        elif user_number > machine_number: 
            print("Too High!")
        else: 
            print("You win!")
            break
        print(f"You have {5 - count} attempts ")
    except ValueError: 
        print("You can only enter an integer number. Try again.")
else: 
    print(f"You lose! The number was {machine_number}")