from tkinter import *


class TTT:

    def __init__(self, master):
        self.buttons = []
        self.master = master
        self.board = [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]
        self.curr_player = 'X'
        self.frame = Frame(
            master=self.master
        )
        self.frame.pack()
        for i in range(0, 3):
            temp = []
            for j in range(0, 3):
                btn = Button(
                    master=self.frame,
                    text='',
                    command=lambda x=i, y=j: self.handle_click(x, y)
                )
                btn.grid(row=i, column=j, padx=5, pady=5)
                temp.append(btn)
            self.buttons.append(temp)

    def handle_click(self, x, y):
        if self.board[x][y] == '':
            print(x, y)
            self.board[x][y] = self.curr_player
            self.buttons[x][y].config(text=self.curr_player)
            if self.win_check() or self.tie_check():
                self.game_over()
            else:
                self.switch_player()

    def switch_player(self):
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
        if self.board[0][2] == self.board[1][1] == self.board[2][0] !='':
            return True
        return False

    def tie_check(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == '':
                    return False
        return True

    def game_over(self):
        for i in range(0, 3):
            for j in range(0, 3):
                self.buttons[i][j].config(state="disabled")
        if self.win_check():
            Label(
                master=self.frame,
                text='Winner is: ' + self.curr_player
            ).grid(row=3, column=1)
        else:
            Label(
                master=self.frame,
                text="Tie"
            ).grid(row=3, column=1)
        self.curr_player = 'X'


root = Tk()
root.title("Tic Tac Toe")
root.geometry("400x400")
t = TTT(root)

root.mainloop()
