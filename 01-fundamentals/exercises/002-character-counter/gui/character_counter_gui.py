import tkinter as tk

root = tk.Tk()
root.title ("Character Counter")
root.geometry("500x300")

tk.Label(
    root, 
    font=("Arial", 10, "normal"), 
    text="Enter a text:"
    ).grid(
    row=0, 
    column=0,
    padx=(50,50), 
    pady=(10,0), 
    sticky="w"
)
text_input = tk.Text(root, height=10, width=50, bg="#ffffff")
text_input.grid(row=1, column=0, padx=(50,50), pady=(10,20))

def get_text():
    user_text = text_input.get("1.0", "end-1c")
    label.config(text=f"Characters: {len(user_text)}")

boton = tk.Button(root, text="Get Characters", bg="#6ac6fc", fg="#0a141a", command=get_text, font=("Arial", 9, "normal"))
boton.grid(row=2, column=0)

label= tk.Label(root, font=("Arial", 10, "bold"), text="Characters: 0")
label.grid(row=3, column=0)
root.mainloop()