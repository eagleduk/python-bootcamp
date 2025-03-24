from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=20, pady=20, bg="white")
window.title("Password Manager")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
bg_image = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=bg_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)

id_label = Label(text="Email/Username:", bg="white")
id_label.grid(row=2, column=0)

id_input = Entry(width=35)
id_input.grid(row=2, column=1, columnspan=2)

pw_label = Label(text="Password:", bg="white")
pw_label.grid(row=3, column=0)

pw_input = Entry(width=21)
pw_input.grid(row=3, column=1)

pw_button = Button(text="Generate Password")
pw_button.grid(row=3, column=2)

add_button = Button(text="Add", width=35)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()