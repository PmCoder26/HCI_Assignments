from tkinter import *
import sympy as sp


class CalculatorPractice:
    def __init__(self):
        self.expression = "0"
        self.list = [
            ["AC", "%", "<-", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["00", "0", ".", "="]
        ]
        self.resultLabel = Label(
            master=root
        )
        self.resultLabel.pack()
        self.frame = Frame(
            master=root
        )
        self.frame.pack()
        for i in range(0, len(self.list)):
            temp = self.list[i]
            for j in range(0, len(temp)):
                btn = Button(
                    master=self.frame,
                    text=temp[j],
                    command=lambda e=temp[j]: self.updateExp(e)
                )
                btn.grid(row=i, column=j, padx=5)

    def updateExp(self, e):
        if e == "AC":
            self.expression = "0"
        if self.expression == "0":
            self.expression = e
        elif e == "=":
            self.expression = sp.simplify(self.expression)
        elif e == "<-":
            self.expression = self.expression[0: len(self.expression) - 1]
        else:
            self.expression += e
        self.resultLabel.config(text=self.expression)


root = Tk()
root.title("Calculator")
root.minsize(width=300, height=300)
root.maxsize(width=600, height=600)
CalculatorPractice()
root.mainloop()
