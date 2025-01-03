import tkinter as tk

class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.create_widgets()

    def create_widgets(self):
        self.buttons = [[tk.Button(self.window, text="", font=("Arial", 20), height=2, width=5, 
                                   command=lambda r=r, c=c: self.make_move(r, c)) 
                         for c in range(3)] for r in range(3)]
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].grid(row=r, column=c)

    def make_move(self, row, col):
        if self.board[row][col] == "" and self.check_winner() is None:
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            self.current_player = "O" if self.current_player == "X" else "X"
        winner = self.check_winner()
        if winner:
            print(f"Player {winner} wins!")

    def check_winner(self):
        # کد بررسی برنده را اینجا قرار دهید.
        return None

    def run(self):
        self.window.mainloop()

# اجرای بازی
game = TicTacToeGUI()
game.run()
