import tkinter

window = tkinter.Tk()
window.title("My first TK")
window.minsize(width=500, height=300)

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

# Entry

input = tkinter.Entry(width=10)
input.pack()

window.mainloop()