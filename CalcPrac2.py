from tkinter import *


class Calc:

    def __init__(self, master):
        self.master = master
        self.data = [
            ['AC', '%', '<-', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['00', '0', '.', '=']
        ]
        self.result = ''
        self.resultLable = Label(
            master=self.master,
            text=self.result
        )
        self.resultLable.pack()
        self.labelFrame = Frame(
            master=self.master
        )
        self.labelFrame.pack()
        for i in range(0, len(self.data)):
            temp = self.data[i]
            for j in range(0, len(temp)):
                Button(
                    master=self.labelFrame,
                    text=temp[j],
                    command=lambda e=temp[j]: self.handleClick(e)
                ).grid(padx=5, pady=5, row=i, column=j)

    def handleClick(self, e):
        if e == 'AC':
            self.result = ''
        elif e == '=':
            self.result = eval(self.result)
        elif e == '<-':
            self.result = self.result[0:len(self.result) - 1]
        else:
            self.result += e
        self.resultLable.config(text=self.result)

root = Tk()
root.geometry("400x400")
root.title("Calculator")

c = Calc(root)


root.mainloop()