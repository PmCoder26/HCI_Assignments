from tkinter import *
import random


class ColorMatching:

    def __init__(self, master):
        self.randomColor = None
        self.master = master
        self.score = 0
        self.wrong_attempts = 0
        self.colorButtons = []
        self.colors = ["red", "green", "blue", "yellow", "purple", "orange"]
        Label(
            master=self.master,
            text="Match the color"
        ).pack()
        self.scoreLabel = Label(
            master=self.master,
            text="Score: " + str(self.score)
        )
        self.scoreLabel.pack()
        self.wrongAttemptsLabel = Label(
            master=self.master,
            text="Wrong Attempts: " + str(self.wrong_attempts)
        )
        self.wrongAttemptsLabel.pack()
        self.matchColorLabel = Label(
            master=self.master,
            text=""
        )
        self.matchColorLabel.pack()
        self.show_random()

        self.colorsFrame = Frame(
            master=root
        )
        self.colorsFrame.pack()
        for i in range(0, len(self.colors)):
            colorButton = Button(
                master=self.colorsFrame,
                text=self.colors[i],
                command=lambda color=self.colors[i]: self.handle_click(color)
            )
            colorButton.grid(row=0, column=i, padx=5)
            self.colorButtons.append(colorButton)

    def show_random(self):
        self.randomColor = random.choice(self.colors)
        self.matchColorLabel.config(text=self.randomColor, fg=random.choice(self.colors))

    def handle_click(self, color):
        if self.randomColor == color:
            self.score += 1
            self.scoreLabel.config(text="Score: " + str(self.score))
            self.show_random()
        else:
            if self.wrong_attempts == -2:
                for i in range(0, len(self.colorButtons)):
                    self.colorButtons[i].config(state="disabled")
                Label(
                    master=self.colorsFrame,
                    text="Game Over!"
                ).grid(row=1, column=3)
                Label(
                    master=self.colorsFrame,
                    text="Your Score: " + str(self.score)
                ).grid(row=2, column=3)
                self.wrong_attempts = 0
                self.score = 0
                self.wrongAttemptsLabel.config(text="")
                self.scoreLabel.config(text="")
                self.matchColorLabel.config(text="")
            else:
                self.wrong_attempts -= 1
                self.wrongAttemptsLabel.config(text="Wrong Attempts: " + str(self.wrong_attempts))
                self.show_random()


root = Tk()
root.title("Color Matching Game")
root.minsize(width=300, height=300)
root.maxsize(width=600, height=600)
game = ColorMatching(root)
root.mainloop()
