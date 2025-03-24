from tkinter import *
from tkinter import messagebox
import random

from pandas.io.clipboard import clipboard_set

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_generator():
    pw_list = [random.choice(letters) for _ in range(0, random.randint(8, 10))]
    pw_list += [random.choice(numbers) for _ in range(0, random.randint(2, 4))]
    pw_list += [random.choice(symbols) for _ in range(0, random.randint(2, 4))]

    random.shuffle(pw_list)
    password = "".join(pw_list)

    pw_input.delete(0, END)
    pw_input.insert(0, password)

    clipboard_set(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    id = id_input.get()
    pw = pw_input.get()

    if len(website) == 0 or len(id) == 0 or len(pw) == 0:
        messagebox.showerror(title="Invalid Input", message="Check Input Data")
        return

    confirm = messagebox.askokcancel(title=website, message="Save ID / PW ?")

    if confirm:
        with open("data.txt", mode="a") as file:
            content = f"{website} : {id} / {pw} \n"
            file.write(content)

        website_input.delete(0, END)
        pw_input.delete(0, END)
        website_input.focus()

        messagebox.showinfo(title="success", message="Save Success.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50, bg="white")
window.title("Password Manager")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
bg_image = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=bg_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)

website_input = Entry(width=45)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

id_label = Label(text="Email/Username:", bg="white")
id_label.grid(row=2, column=0)

id_input = Entry(width=45)
id_input.insert(0, "test@email.com")
id_input.grid(row=2, column=1, columnspan=2)

pw_label = Label(text="Password:", bg="white")
pw_label.grid(row=3, column=0)

pw_input = Entry(width=28)
pw_input.grid(row=3, column=1)

pw_button = Button(text="Generate Password", width=15, command=password_generator)
pw_button.grid(row=3, column=2)

add_button = Button(text="Add", width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()