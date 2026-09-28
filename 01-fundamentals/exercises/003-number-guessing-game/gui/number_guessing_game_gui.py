import tkinter as tk
import random 

root = tk.Tk()
root.title("Number Guessing Game") 
root.geometry("500x300")
root.grid_columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

game_frame = tk.Frame(root)
game_frame.grid(row=0, column=0 )

machine_number = random.randint(1,100)

title_game = tk.Label(
    game_frame,
    text="Number Guessing Game"
    ).grid(
    row=0,
    column=0,
    pady=(30,10),
    sticky="w"
)
rules = tk.Label(
   game_frame,
    text="Guess a number between 1 and 100:",
    font=("Inter", 10)
).grid(
    row=1,
    column=0,
    pady=(10,10),
    sticky="w"
)
user_input = tk.Entry(
    game_frame,
    width=10,
    bg="#ffffff",
   justify = "center"
)
user_input.grid(
    row=2, 
    column=0,
    pady=(0,0) 
)

count = 0
def check_guess():
    global count
    try: 
        user_number = int(user_input.get())
             
    except ValueError: 
        warning_label.config(text="You can only enter an integer number. Try again.")
        return     
    
    if user_number  not in range(1,101):
        warning_label.config(text="Enter a number between 1 and 100.")
        return
    
    warning_label.config(text="")
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
    user_input.delete(0,tk.END)
    user_input.focus_set()
    attempts_label.config(text=f"Attempts left: {5-count}")
        
guess_boton = tk.Button(game_frame, width=10, bg="#6ac6fc", fg="#0a141a", text="Guess", command=check_guess)
guess_boton.grid(row=3, column=0, pady=(10,0))

hint_label = tk.Label(game_frame, text="")
hint_label.grid(row=4, column=0, pady=(0,0))

warning_label = tk.Label(game_frame)
warning_label.grid(row=5, column=0, pady=(0,0))

attempts_label = tk.Label( game_frame, text="Attempts left: 5")
attempts_label.grid(row=6, column=0, pady=(0,0))

root.mainloop()