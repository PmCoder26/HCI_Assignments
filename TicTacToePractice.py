from tkinter import *



class TTT:
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
                btn = Button(
                    master=self.master,
                    text='',
                    command=lambda x=i, y=j: self.handle_click(x, y)
                )
                btn.grid(row=i, column=j)
                temp.append(btn)
            self.buttons.append(temp)

    def handle_click(self, i, j):
        if self.board[i][j] == '':
            self.board[i][j] = self.curr_player
            self.buttons[i][j].config(text=self.curr_player)
            if self.win_check() or self.tie_check():
                self.game_over()
            else:
                self.swtich_player()

    def switch_player(self):
        if self.curr_player == 'X':
            self.curr_player = 'O'
        else:
            self.curr_player = 'X'

    def win_check(self):
        # Row check.
        for i in range(0, 3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True

        # Column check
        for i in range(0, 3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True

        # Diagonal check.
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

        return False


root = Tk()
root.title="Tic Tac Toe"
TTT(root)

root.mainloop()