import random
import os

def num_dice():
    while True:
        try:
            num_dice = input("Number of dice")
            valid_responnses = ['1', 'one', 'two', '2']
            if num_dice not in valid_responnses:
                raise ValueError("lower z only")
            else:
                return num_dice
        except ValueError as err:
            print(err)

def roll_dice():
    
