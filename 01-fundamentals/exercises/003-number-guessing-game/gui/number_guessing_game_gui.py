import tkinter as tk
import random 

root = tk.Tk()
root.title("Number Guessing Game") 
root.geometry("500x300")

machine_number = random.randint(1,100)

title_game = tk.Label(
    root,
    text="Number Guessing Game"
    ).grid(
    row=0,
    column=0
)
rules = tk.Label(
    root, 
    text="Guess a number between 1 and 100:"
).grid(
    row=1,
    column=0
)
user_input = tk.Entry(root)
user_input.grid(row=2, column=0)

count = 0
def check_guess():
    global count
    user_number = int(user_input.get())
    count += 1 

    if count == 5 and user_number != machine_number:
        hint_label.config(text=f"You lose! The number was {machine_number}")
        guess_boton.config(state="disabled")
    else: 
        if user_number < machine_number: 
            hint_label.config(text="Too Low!") 
        elif user_number > machine_number: 
            hint_label.config(text="Too High!") 
        else: 
            guess_boton.config(state="disabled")
            hint_label.config(text="You win!")

    attempts_label.config(text=f"Attempts left: {5-count}")
        
guess_boton = tk.Button(root, text="Guess", command=check_guess)
guess_boton.grid(row=3, column=0)

hint_label = tk.Label(root, text="")
hint_label.grid(row=4, column=0)

attempts_label = tk.Label(root, text="Attempts left: 5")
attempts_label.grid(row=5, column=0)

root.mainloop()