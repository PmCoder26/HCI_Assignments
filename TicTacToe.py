from tkinter import *
from tkinter.ttk import *


class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.board = [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]
        self.curr_player = 'X'
        self.buttons = []
        for i in range(0, 3):
            temp = []
            for j in range(0, 3):
                boardCell = Button(
                    master=self.master,
                    text="",
                    command=lambda x=i, y=j: self.handle_click(x, y)
                )
                boardCell.grid(row=i, column=j, padx=1, pady=1)
                temp.append(boardCell)
            self.buttons.append(temp)

    def handle_click(self, i, j):
        if self.board[i][j] == '':
            self.board[i][j] = self.curr_player
            self.buttons[i][j].configure(text=self.board[i][j])
            if self.win_check() or self.tie_check():
                self.game_over()
            else:
                self.player_switch()

    def player_switch(self):
        if self.curr_player == 'X':
            self.curr_player = 'O'
        else:
            self.curr_player = 'X'

    def win_check(self):
        #         Row check.
        for i in range(0, 3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True

        #         Column check.
        for j in range(0, 3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] != '':
                return True

        #         Diagonal check.
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True

        return False

    def tie_check(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == '':
                    return False
                else:
                    continue
        return True

    def game_over(self):
        for i in range(0, 3):
            for j in range(0, 3):
                self.buttons[i][j].configure(state="disabled")
        if self.win_check():
            Label(
                master=self.master,
                text="The winner is: " + self.curr_player
            ).grid(row=3, column=1)
        else:
            Label(
                master=self.master,
                text="Tie"
            ).grid(row=3, column=1)
        self.curr_player = 'X'


root = Tk()
root.title("Tic Tac Toe")
root.minsize(width=300, height=300)
root.maxsize(width=600, height=600)
game = TicTacToe(root)
root.mainloop()
