import sys
import turtle
import tkinter as tk
import numpy as nm
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Pacman Game With Artificial Intelligence")
wn.setup(700,700)
#turtle=turtle.Turtle()
#turtle.shape("circle")
#turtle.pen(fillcolor="black", pencolor="yellow", pensize=10)
#tk.mainloop()

#register shapes
turtle.register_shape("map.gif")


#maze yarat
class Maze(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("map.gif")
        self.pen(fillcolor="black", pencolor="yellow", pensize=10)
        self.penup()
        self.speed(0)

def create_fruit_or_food():
    randomVal=nm.random.randomint(601,size=1)
    print()


def create_maze(grid):
    for y in range(len(grid)):                      #Labirent İçin Kodlanan Grid'in Tüm Birimleri Çizilecek
        for x in range(len(grid[y])):                
            character = grid[y][x]                   
            screen_x = -588 + (x * 24)   #Her Bir Square 24x24 Bit       
            screen_y = 288 - (y * 24)    #Ekrandaki Maze Tam Center'lı Gibi Düşünülmeli Analitik Düzlem Üzerinde             

            if character == "+":                     
                maze.goto(screen_x, screen_y)        
                maze.stamp()   #Elemanın Ekranda Kalmasını Sağlıyor Stampleniyor                      
                #walls.append((screen_x, screen_y))   
            
grid = [
#Grid İçinde Rastgele Bir Yere Elaman Eklenirken Bunu Grid Üzerinde Boş Olen Yerlerden Birine Yapıcaz.
"++++++++++++++++++++++++++++++++++++++++", 
"+P              T+++++++               +",
"+ ++++++ +++++++ +++++++ +++++++ +++++ +",
"+                                      +",
"+ ++++++ ++ +++++++++++++++++ ++ +++++ +",
"+        ++      +++++++      ++       +",
"++++++++ +++++++ +++++++ +++++++ +++++++",
"++++++++ ++                   ++ +++++++",
"++++++++ ++ ++++++++ ++++++++ ++ +++++++",
"+                                      +",
"++++++++ ++ ++++++++ ++++++++ ++ +++++++",
"++++++++ ++                   ++ +++++++",
"++++++++ ++ +++++++++++++++++ ++ +++++++",
"+                +++++++               +",
"+ ++++++ +++++++ +++++++ +++++++ +++++ +",
"+     ++                         ++    +",
"+++++ ++ +++++++ +++++++ +++++++ ++ ++++",
"+        +++++++    +    +++++++       +",
"+ +++++++++++++++++ + ++++++++++++++++ +",
"+                                      +",
"++++++++++++++++++++++++++++++++++++++++",

]
maze=Maze()
walls=[]
foods=[]
create_maze(grid)


tk.mainloop()

