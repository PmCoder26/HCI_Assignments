from tkinter import *
import sympy as sp

list = [
    ["AC", "%", "<-", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["00", "0", ".", "="]
]

expression = "0"


def updateExpression(op):
    global expression
    if expression == "0":
        expression = op
    elif op == "=":
        expression = sp.simplify(expression)
        label.configure(text=expression)
    elif op == "AC":
        expression = "0"
    elif op == "<-":
        expression = expression[0 : len(expression) - 1]
    else:
        expression += op
    label.configure(text=expression)


root = Tk()
root.title("Calculator")
root.geometry("600x600")

label = Label(
    master=root,
    text=expression,
    font=("Arial", 24)
)
label.pack(pady=20)

frame = Frame(master=root)

for i in range(0, len(list)):
    temp = list[i]
    for j in range(0, len(temp)):
        button = Button(
            master=frame,
            text=temp[j],
            command=lambda t=temp[j]: updateExpression(t),
            height=3,
            width=5
        )
        button.grid(row=i, column=j)
frame.pack()

root.mainloop()
