import sys
import turtle
import tkinter as tk
import random
import ctypes
user32 = ctypes.windll.user32
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Pacman Game With Artificial Intelligence")
wn.setup(width=.99,height=.90,startx=0,starty=0)


class Maze(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.pen(fillcolor="black", pencolor="yellow", pensize=10)
        self.penup()
        self.speed(0)

class Fruit_Food(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.pen(fillcolor="black", pencolor="yellow", pensize=0)
        self.penup()


#def create_fruit_or_food():
 #       if random.randint(0,len(grid),random.randint(0,len(grid[0])) not in walls              #20 46
            

def create_maze(grid):
    for y in range(len(grid)):                      #Labirent İçin Kodlanan Grid'in Tüm Birimleri Çizilecek
        for x in range(len(grid[y])):                
            character = grid[y][x]                   
            screen_x = -552 + (x * 24)   #Her Bir Square 24x24 Bit       
            screen_y = 288 - (y * 24)    #Ekrandaki Maze Tam Center'lı Gibi Düşünülmeli Analitik Düzlem Üzerinde             

            if character == "+":                     
                maze.goto(screen_x, screen_y)        
                maze.stamp()   #Elemanın Ekranda Kalmasını Sağlıyor Stampleniyor                      
                walls.append((screen_x, screen_y))  
            
grid = [
"++++++++++++++++++++++++++++++++++++++++++++++", #Grid İçinde Rastgele Bir Yere Elaman Eklenirken Bunu Grid Üzerinde Boş Olen Yerlerden Birine Yapıcaz.
"+ s             +                            +", #20*46 =920 Character
"+  ++++++++++  +++++++++++++  +++++++  ++++  +",
"+           +                 +        +     +",
"+  +++++++  +++++++++++++  +++++++++++++++++++",
"+  +     +  +           +  +                 +",
"+  +  +  +  +  +  ++++  +  +  +++++++++++++  +",
"+  +  +  +  +  +  +     +  +  +  +        +  +",
"+  +  ++++  +  ++++++++++  +  +  ++++  +  +  +",
"+  +     +  +              +           +  +  +",
"+  ++++  +  ++++++++++++++++  +++++++++++++  +",
"+     +  +                    +              +",
"++++  +  ++++++++++++++++++++++  ++++++++++  +",
"+  +  +                    +     +     +  +  +",
"+  +  ++++  +++++++++++++  +  ++++  +  +  +  +",
"+  +  +     +     +     +  +  +     +     +  +",
"+  +  +  +++++++  ++++  +  +  +  ++++++++++  +",
"+                       +  +  +              +",
"++++  +  +  ++++++++++  +  +  +  +++++++++++++",
"+++++++++++++++++++++++e++++++++++++++++++++++",
]
maze=Maze()
walls=[]
create_maze(grid)


tk.mainloop()

