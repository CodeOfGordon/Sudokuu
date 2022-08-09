import random
from copy import *
#problem: problem doesnt finish running, maybe impossible board rabbit hole or too long???

def create_board():
    row_1=[0,0,0,0,0,0,0,0,0]
    row_2=[0,0,0,0,0,0,0,0,0]
    row_3=[0,0,0,0,0,0,0,0,0]
    row_4=[0,0,0,0,0,0,0,0,0]
    row_5=[0,0,0,0,0,0,0,0,0]
    row_6=[0,0,0,0,0,0,0,0,0]
    row_7=[0,0,0,0,0,0,0,0,0]
    row_8=[0,0,0,0,0,0,0,0,0]
    row_9=[0,0,0,0,0,0,0,0,0]
    column_1=[row_1[0],row_2[0],row_3[0],row_4[0],row_5[0],row_6[0],row_7[0],row_8[0],row_9[0]]
    column_2=[row_1[1],row_2[1],row_3[1],row_4[1],row_5[1],row_6[1],row_7[1],row_8[1],row_9[1]]
    column_3=[row_1[2],row_2[2],row_3[2],row_4[2],row_5[2],row_6[2],row_7[2],row_8[2],row_9[2]]
    column_4=[row_1[3],row_2[3],row_3[3],row_4[3],row_5[3],row_6[3],row_7[3],row_8[3],row_9[3]]
    column_5=[row_1[4],row_2[4],row_3[4],row_4[4],row_5[4],row_6[4],row_7[4],row_8[4],row_9[4]]
    column_6=[row_1[5],row_2[5],row_3[5],row_4[5],row_5[5],row_6[5],row_7[5],row_8[5],row_9[5]]
    column_7=[row_1[6],row_2[6],row_3[6],row_4[6],row_5[6],row_6[6],row_7[6],row_8[6],row_9[6]]
    column_8=[row_1[7],row_2[7],row_3[7],row_4[7],row_5[7],row_6[7],row_7[7],row_8[7],row_9[7]]
    column_9=[row_1[8],row_2[8],row_3[8],row_4[8],row_5[8],row_6[8],row_7[8],row_8[8],row_9[8]]
    box_1=[row_1[0],row_1[1],row_1[2],row_2[0],row_2[1],row_2[2],row_3[0],row_3[1],row_3[2]]
    box_2=[row_1[3],row_1[4],row_1[5],row_2[3],row_2[4],row_2[5],row_3[3],row_3[4],row_3[5]]
    box_3=[row_1[6],row_1[7],row_1[8],row_2[6],row_2[7],row_2[8],row_3[6],row_3[7],row_3[8]]
    box_4=[row_4[0],row_4[1],row_4[2],row_5[0],row_5[1],row_5[2],row_6[0],row_6[1],row_6[2]]
    box_5=[row_4[3],row_4[4],row_4[5],row_5[3],row_5[4],row_5[5],row_6[3],row_6[4],row_6[5]]
    box_6=[row_4[6],row_4[7],row_4[8],row_5[6],row_5[7],row_5[8],row_6[6],row_6[7],row_6[8]]
    box_7=[row_7[0],row_7[1],row_7[2],row_8[0],row_8[1],row_8[2],row_9[0],row_9[1],row_9[2]]
    box_8=[row_7[3],row_7[4],row_7[5],row_8[3],row_8[4],row_8[5],row_9[3],row_9[4],row_9[5]]
    box_9=[row_7[6],row_7[7],row_7[8],row_8[6],row_8[7],row_8[8],row_9[6],row_9[7],row_9[8]]
    rows=[row_1,row_2,row_3,row_4,row_5,row_6,row_7,row_8,row_9]
    columns=[column_1,column_2,column_3,column_4,column_5,column_6,column_7,column_8,column_9]
    boxes=[box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9]

    row_count = 0
    position=0
    while row_count != 9:
        number = random.randint(1,9)
        if number not in rows[row_count]:
            if number not in columns[row_count]:
                if number not in boxes[row_count]:
                    rows[row_count][position] = number
                    position+=1

                    rows,columns,boxes = update_lists(rows,columns,boxes)
                    column_1 = columns[0]
                    column_2 = columns[1]
                    column_3 = columns[2]
                    column_4 = columns[3]
                    column_5 = columns[4]
                    column_6 = columns[5]
                    column_7 = columns[6]
                    column_8 = columns[7]
                    column_9 = columns[8]
                    box_1 =boxes[0]
                    box_2= boxes[1]
                    box_3= boxes[2]
                    box_4= boxes[3]
                    box_5= boxes[4]
                    box_6= boxes[5]
                    box_7= boxes[6]
                    box_8= boxes[7]
                    box_9= boxes[8]

        if position == 9:
            position = 0
            row_count += 1
    print(rows)
    print(column_1)

def update_lists(rows,columns,boxes):
    row_1 = rows[0]
    row_2 = rows[1]
    row_3 = rows[2]
    row_4 = rows[3]
    row_5 = rows[4]
    row_6 = rows[5]
    row_7 = rows[6]
    row_8 = rows[7]
    row_9 = rows[8]
    column_1=[row_1[0],row_2[0],row_3[0],row_4[0],row_5[0],row_6[0],row_7[0],row_8[0],row_9[0]]
    column_2=[row_1[1],row_2[1],row_3[1],row_4[1],row_5[1],row_6[1],row_7[1],row_8[1],row_9[1]]
    column_3=[row_1[2],row_2[2],row_3[2],row_4[2],row_5[2],row_6[2],row_7[2],row_8[2],row_9[2]]
    column_4=[row_1[3],row_2[3],row_3[3],row_4[3],row_5[3],row_6[3],row_7[3],row_8[3],row_9[3]]
    column_5=[row_1[4],row_2[4],row_3[4],row_4[4],row_5[4],row_6[4],row_7[4],row_8[4],row_9[4]]
    column_6=[row_1[5],row_2[5],row_3[5],row_4[5],row_5[5],row_6[5],row_7[5],row_8[5],row_9[5]]
    column_7=[row_1[6],row_2[6],row_3[6],row_4[6],row_5[6],row_6[6],row_7[6],row_8[6],row_9[6]]
    column_8=[row_1[7],row_2[7],row_3[7],row_4[7],row_5[7],row_6[7],row_7[7],row_8[7],row_9[7]]
    column_9=[row_1[8],row_2[8],row_3[8],row_4[8],row_5[8],row_6[8],row_7[8],row_8[8],row_9[8]]
    box_1=[row_1[0],row_1[1],row_1[2],row_2[0],row_2[1],row_2[2],row_3[0],row_3[1],row_3[2]]
    box_2=[row_1[3],row_1[4],row_1[5],row_2[3],row_2[4],row_2[5],row_3[3],row_3[4],row_3[5]]
    box_3=[row_1[6],row_1[7],row_1[8],row_2[6],row_2[7],row_2[8],row_3[6],row_3[7],row_3[8]]
    box_4=[row_4[0],row_4[1],row_4[2],row_5[0],row_5[1],row_5[2],row_6[0],row_6[1],row_6[2]]
    box_5=[row_4[3],row_4[4],row_4[5],row_5[3],row_5[4],row_5[5],row_6[3],row_6[4],row_6[5]]
    box_6=[row_4[6],row_4[7],row_4[8],row_5[6],row_5[7],row_5[8],row_6[6],row_6[7],row_6[8]]
    box_7=[row_7[0],row_7[1],row_7[2],row_8[0],row_8[1],row_8[2],row_9[0],row_9[1],row_9[2]]
    box_8=[row_7[3],row_7[4],row_7[5],row_8[3],row_8[4],row_8[5],row_9[3],row_9[4],row_9[5]]
    box_9=[row_7[6],row_7[7],row_7[8],row_8[6],row_8[7],row_8[8],row_9[6],row_9[7],row_9[8]]
    rows=[row_1,row_2,row_3,row_4,row_5,row_6,row_7,row_8,row_9]
    columns=[column_1,column_2,column_3,column_4,column_5,column_6,column_7,column_8,column_9]
    boxes=[box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9]
    return rows,columns,boxes


create_board()