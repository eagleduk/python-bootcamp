import tkinter

window = tkinter.Tk()
window.title("My first TK")
window.minsize(width=500, height=600)

# Label
label = tkinter.Label(text="Hello", font=24)
label.pack()

# Button
def button_click():
    label["text"] = "Button Got Clicked"
    input_text = input.get()
    print(input_text)

button = tkinter.Button(text="click me", command=button_click)
button.pack()

# Entry - input

input = tkinter.Entry(width=10)
input.pack()

# Text - Text Area

text = tkinter.Text(width=10, height=4)
text.pack()

# Scale - Range
scale = tkinter.Scale()
scale.pack()

# Spinbox - input[number]
spin_box = tkinter.Spinbox(from_=0, to=100, width=4)
spin_box.pack()

# Check - input[check]
check_state = tkinter.IntVar()
check1 = tkinter.Checkbutton(variable=check_state)
check1.pack()

# Radio
radio_state = tkinter.IntVar()
radio1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state)
radio2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state)
radio1.pack()
radio2.pack()

# List
list = tkinter.Listbox()
list.insert(1, "1")
list.insert(2, "2")
list.insert(3, "3")
list.pack()

window.mainloop()