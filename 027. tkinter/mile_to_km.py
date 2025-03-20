import tkinter as T

window = T.Tk()
window.minsize(width=300, height=120)
window.config(padx=40, pady=30)
window.title("Mile to Km Converter")

# 1.60934
def calculate_mile_to_km():
    mile = entry.get()
    km = int(mile) * 1.60934
    km_value["text"] = km

# Mile Entry
entry = T.Entry()
entry.grid(row=0, column=1)
entry.focus()

# Mile Unit Label
mile_label = T.Label(text="Miles")
mile_label.grid(row=0, column=2)

# Label
label = T.Label(text="is equal to")
label.grid(row=1, column=0)

# Km Value Label
km_value = T.Label(text="0")
km_value.grid(row=1, column=1)

# Km Unit Label
km_label = T.Label(text="Km")
km_label.grid(row=1, column=2)

# Convert Button
button = T.Button(text="Calculate", command=calculate_mile_to_km)
button.grid(row=2, column=1)

window.mainloop()
