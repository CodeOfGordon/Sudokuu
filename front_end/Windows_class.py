from tkinter import *
from PIL import ImageTk, Image # for image
import os

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

        self.submit()
        self.emoji_ind()
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
                self.small_box = Entry(self.big_box, width=10) # Turn into entry box
                #self.small_box.config(width=self.small_box_width-self.small_box_border, height=self.small_box_height-self.small_box_border, bg="#E8E651")
                self.small_box.place(x=j*(self.small_box_width+self.small_box_border), y=i*(self.small_box_height+self.small_box_border))
        
    def emoji_ind(self):
        ''' Emoji that will indicate whether the game is won or not '''
        emoji = Image.open("front_end/thinking_emoji.png")
        emojier = ImageTk.PhotoImage(emoji)
        

        self.emoji_label = Label(image=emojier)
        self.emoji_label.image = emojier
        self.emoji_label.place(x=(MENU_WIDTH/1.5), y=(MENU_HEIGHT/15))
    
    def message_box(self):
        ''' Message box that will display the message '''
        self.message_box = Label(self.root, text="Solve the Sudoku puzzle!", font=("Arial", 20))
        self.message_box.place(x=(MENU_WIDTH/1.5), y=(MENU_HEIGHT/2))

    def submit(self):
        ''' Submit button '''
        self.submit_button = Button(self.root, text="Submit", font=("Arial", 20), bg="#32CD32")
        self.submit_button.place(x=(MENU_WIDTH/1.7), y=(MENU_HEIGHT/2), width=((MENU_WIDTH/2)-BORDER_SIZE), height=50)
        

if __name__ == '__main__':
    window = Windows()
    window.root.mainloop()


