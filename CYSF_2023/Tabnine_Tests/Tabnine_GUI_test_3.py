## python tic tac toe game in tkinter

import tkinter as tk

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("300x300")

board = tk.Canvas(root, width=300, height=300)
board.pack()

def draw_board():
    board.delete("all")
    for i in range(3):
        for j in range(3):
            if i == 0 and j == 0:
                board.create_rectangle(j*100, i*100, (j+1)*100, (i+1)*100, fill="black")
            elif i == 0 and j == 2:
                board.create_rectangle(j*100, i*100, (j+1)*100, (i+1)*100, fill
                                       ="black")
                board.create_rectangle(j*100, i*100, (j+1)*100, (i+1)*100, fill="black")
            elif i == 2 and j == 0:
                board.create_rectangle(j*100, i*100, (j+1)*100, (i+1)*100, fill="black")

            elif i == 2 and j == 2:
                board.create_rectangle(j*100, i*100, (j+1)*100, (i+1)*100, fill="black")
                board.create_rectangle(j*100, i*100, (j+1)*100, (i+1)*100, fill="black")

            elif i == 0 and j == 1:
                board.create_rectangle(j*100, i*100, (j+1)*100, (i+1)*100, fill="black")
    
            elif i == 1 and j == 0:
                board.create_rectangle(j*100, i*100, (j+1)*100, (i+1)*100, fill="black")
    
            elif i == 1 and j == 2:
                board.create_rectangle(j*100, i*100, (j+1)*100, (i+1)*100, fill="black")
                
                
    
    