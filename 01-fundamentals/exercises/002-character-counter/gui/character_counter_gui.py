import tkinter as tk

root = tk.Tk()
root.title ("Character Counter")
root.geometry("500x300")

tk.Label(root, text="Enter a text:").grid(row=0, column=0)
text_input = tk.Text(root, height=10, width=50)
text_input.grid(row=1, column=0)

def get_text():
    user_text = text_input.get("1.0", "end-1c")
    label.config(text=f"Characters: {len(user_text)}")
    
boton = tk.Button(root, text="Obtener Texto", command=get_text)
boton.grid(row=2, column=0)

label= tk.Label(root, text="Characters: 0")
label.grid(row=3, column=0)
root.mainloop()