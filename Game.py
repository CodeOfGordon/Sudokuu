from cgitb import small
from back_end.collections_class import *
from front_end.Windows_class import *
from tkinter import *


class Game:
    ''' Main game functions '''
    def __init__(self):
        self.window = Windows()
        self.functionality()

    def receive_input(self): # PROBLEM
        '''Receives input from the sudoku board'''
        board = []
        print(self.window.all_entry_boxes.get())
        for box in self.window.entry_boxes:
            #small_box_num = self.window.small_box.get()
            board.append(box.get())
        print(board)

    def functionality(self):
        '''Functionality of the widgets'''
        self.window.submit_button["command"] = self.receive_input


if __name__ == '__main__':
    game = Game()
    game.window.root.mainloop()