import tkinter as tk
from tkinter import messagebox 

class TicTakToeGUI:
    def __init__(self, board_size=3):
        self.boars_size = board_size
        self.window = tk.Tk()
        self.window.title('Tic Tak Toe')
        self.board = [[' ' for _ in range(self.boars_size)] for _ in range(self.boars_size)]
        self.current_player = 'X'
        self.create_board_buttons()

    def create_board_buttons(self):
        self.buttons = [[tk.Button(self.window, text=' ', font=('Arial', 24), width=3, height=1,
                                   command= lambda row=row, col=col: self.make_move(row, col)) for col in range(self.boars_size)]
                                   for row in range(self.boars_size)]
        for row in range(self.boars_size):
            for col in range(self.boars_size):
                self.buttons[row][col].grid(row=row, column=col)

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_win(self.current_player):
                pass
            elif self.is_full():
                pass
            else: 
                self.current_player = 'O' if self.current_player == 'X' else 'X'

        else:
            messagebox.showerror("Invalid Move", "Cell already taken. Try again!")

            

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    board_size = int(input("Enter the size of the board(e.g. , 3 for 3x3, 4 for 4x4, etc.): "))
    tic_tac_toe = TicTakToeGUI(board_size)
    tic_tac_toe.run()

