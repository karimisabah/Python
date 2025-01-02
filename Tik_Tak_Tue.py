import tkinter as Tk 
from tkinter import messagebox 

class TicTakTueGUI:
    def __init__(self, board_size=3):
        self.boars_size = board_size
        self.window = tk.Tk()
        self.window.title('Tic Tak Tue')
        self.board = [[' ' for _ in range(self.boars_size)] for _ in range(self.boars_size)]
        self.current_player = 'X'
        self.creat_board_buttons()

    def create_board_buttons(self):
        self.buttons = [[tk.button(self.window, text= ' ', font='Arial', ))]]

