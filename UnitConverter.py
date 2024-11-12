from tkinter import *
from tkinter.ttk import *


def convert():
    global result
    result = 0
    value = float(entry.get())
    typeFrom = fromBox.get()
    typeTo = toBox.get()
    if typeFrom == "Inch":
        result += value * 2.54
        if typeTo == "Meter":
            result /= 100
        elif typeTo == "Kilometer":
            result /= 1000
    elif typeFrom == "Centimeter":
        result = value
        if typeTo == "Meter":
            result /= 100
        elif typeTo == "Kilometer":
            result /= 1000
        elif typeTo == "Inch":
            result /= 2.54
    elif typeFrom == "Meter":
        result = value
        if typeTo == "Centimeter":
            result *= 100
        elif typeTo == "Kilometer":
            result /= 1000
        elif typeTo == "Inch":
            result = (result * 100) / 2.54
    elif typeFrom == "Kilometer":
        result = value
        if typeTo == "Meter":
            result *= 1000
        elif typeTo == "Centimeter":
            result *= 1000 * 100
        elif typeTo == "Inch":
            result = (result * 1000) / 2.54
    resultLabel.configure(text=result)
            

converterList = ["Inch", "Centimeter", "Meter", "Kilometer"]
result = 0.0

root = Tk()
root.title("Length Converter")
root.geometry("500x500")

frame = Frame(
    master=root,
)
frame.pack()

inputLength = Label(
    master=frame,
    text="Input"
)
inputLength.grid(row=0, column=0)

entry = Entry(
    master=frame,
    width=10,
)
entry.grid(row=0, column=1, padx=5)

fromBox = Combobox(
    master=frame,
    values=converterList
)
fromBox.set("Inch")
fromBox.grid(row=0, column=2, padx=5)

toBox = Combobox(
    master=frame,
    values=converterList
)
toBox.set("Centimeter")
toBox.grid(row=0, column=3, padx=5)

resultBtn = Button(
    master=frame,
    text="Result",
    command=convert
)
resultBtn.grid(row=1, column=0, pady=50, padx=5)

resultLabel = Label(
    master=frame,
    text=result,
)
resultLabel.grid(row=1, column=1, pady=50, padx=5)

root.mainloop()
