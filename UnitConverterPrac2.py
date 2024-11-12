from tkinter import *
from tkinter.ttk import Combobox


class UC:

    def __init__(self, master):
        self.converterList = ["Inch", "Centimeter", "Meter", "Kilometer"]
        self.result = 0.0
        self.master = master
        self.frame = Frame(
            master=self.master
        )
        self.frame.pack()
        self.inputLabel = Label(
            master=self.frame,
            text="Input"
        )
        self.inputLabel.grid(row=0, column=0, padx=5, pady=5)
        self.inputEntry = Entry(
            master=self.frame
        )
        self.inputEntry.grid(row=0, column=1, padx=5, pady=5)
        self.fromCombo = Combobox(
            master=self.frame,
            values=self.converterList
        )
        self.fromCombo.grid(row=0, column=2, padx=5, pady=5)
        self.fromCombo.set(self.converterList[0])
        self.toCombo = Combobox(
            master=self.frame,
            values=self.converterList
        )
        self.toCombo.grid(row=0, column=3, padx=5, pady=5)
        self.toCombo.set(self.converterList[0])
        self.resultButton = Button(
            master=self.frame,
            text="Result",
            command=lambda: self.handle_click
        )
        self.resultButton.grid(row=1, column=0, padx=5, pady=5)
        self.resultLabel = Label(
            master=self.frame,
            text=self.result
        )
        self.resultLabel.grid(row=1, column=1, padx=5, pady=5)

    def handle_click(self):
        fromType = self.fromCombo.get()
        toType = self.toCombo.get()
        value = float(self.inputEntry.get())
        if fromType == toType:
            self.result = value
        elif fromType == 'Inch':
            result = value * 2.54
            if toType == 'Meter':
                result /= 100
            elif toType == 'Kilometer':
                result /= 1000
            self.result = result
        elif fromType == 'Centimeter':
            result = value
            if toType == 'Inch':
                result /= 2.54
            elif toType == 'Meter':
                result /= 100
            elif toType == 'Kilometer':
                result /= 1000
            self.result = result
        elif fromType == 'Meter':
            result = value
            if toType == 'Inch':
                result = (result * 100) / 2.54
            elif toType == 'Centimeter':
                result *= 100
            elif toType == 'Kilometer':
                result /= 1000
            self.result = result
        elif fromType == 'Kilometer':
            result = value
            if toType == 'Inch':
                result = (result * 1000) / 2.54
            elif toType == 'Centimeter':
                result *= 1000






root = Tk()
root.title("Unit Converter")
root.geometry("600x400")
u = UC(root)

root.mainloop()

