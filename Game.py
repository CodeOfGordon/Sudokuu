from back_end.collections_class import *
from front_end.Windows_class import *


class Game:
    ''' Main game functions '''
    def __init__(self):
        self.window = Windows()
        self.functionality()
        pass

    def receive_input(self):
        '''Receives input from the sudoku board'''
        board = []
        for i in range(3):
            for j in range(3):
                small_box_num = self.window.small_boxes[i][j].get()
                board.append(small_box_num)
                print(small_box_num)
        print(board)

    def functionality(self):
        '''Functionality of the widgets'''
        self.window.submit["command"] = self.receive_input()


if __name__ == '__main__':
    game = Game()
    game.window.root.mainloop()