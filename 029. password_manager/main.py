from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")
window.minsize(width=220, height=220)

canvas = Canvas(width=200, height=200)
bg_image = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=bg_image)
canvas.pack()

window.mainloop()