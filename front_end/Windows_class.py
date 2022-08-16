from tkinter import *

MENU_WIDTH = 1280
MENU_HEIGHT = 720
BORDER_SIZE = 15


class Windows:
    ''' GUI '''
    def __init__(self):
        self.root = Tk()

        self.root.geometry(f"{MENU_WIDTH}x{MENU_HEIGHT}")
        self.root.title("Sudokuu!")
        self.root.resizable(False,False)

        self.sudoku_board()

    def sudoku_board(self):
        ''' Sudoku board '''
        self.border = Frame(self.root, width=MENU_WIDTH/2, height=MENU_HEIGHT/1.16, bg="#DBBF57") # #33FFEC
        self.border.place(x=(MENU_WIDTH/16), y=(MENU_HEIGHT/16))

        self.board_width = (MENU_WIDTH/2)-(BORDER_SIZE*2)
        self.board_height = (MENU_HEIGHT/1.16)-(BORDER_SIZE*2)

        self.board = Frame(self.border, width=(self.board_width), height=(self.board_height), bg="#DBBF57")
        self.board.place(x=BORDER_SIZE, y=BORDER_SIZE)
        self.big_boxes()

    def big_boxes(self):
        ''' Big boxes inside sudoku board '''
        self.big_box_height = (self.board_height)/3.16
        self.big_box_width = (self.board_width)/3.16
        for i in range(3):
            for j in range(3):
                self.big_box = Frame(self.board, width=self.big_box_width, height=self.big_box_height, bg="#F2E055")
                self.big_box.place(x=j*(self.big_box_width+BORDER_SIZE), y=i*(self.big_box_height+BORDER_SIZE))
                self.small_boxes()

    def small_boxes(self):
        ''' Small boxes inside sudoku board '''
        self.small_box_height = (self.big_box_height)/3
        self.small_box_width = (self.big_box_width)/3
        self.small_box_border = BORDER_SIZE/4

        for i in range(3):
            for j in range(3):
                self.small_box = Frame(self.big_box) # Turn into entry box
                self.small_box.config(width=self.small_box_width-self.small_box_border, height=self.small_box_height-self.small_box_border, bg="#E8E651")
                self.small_box.place(x=j*(self.small_box_width+self.small_box_border), y=i*(self.small_box_height+self.small_box_border))

if __name__ == '__main__':
    window = Windows()
    window.root.mainloop()


