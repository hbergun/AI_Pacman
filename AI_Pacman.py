import turtle
import math
import tkinter
import ctypes
import Heuristic
import queue
import sys
import time

queue=queue.Queue()
visited=[]
res_x=ctypes.windll.user32.GetSystemMetrics(0)
res_y=ctypes.windll.user32.GetSystemMetrics(1)
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Pacman Game With Artificial Intelligence")
wn.setup(width=.99,height=.90,startx=0,starty=0)

#register shapes Konum Değiştir Erken Yapıyor
wn.register_shape("map.gif")
#wn.register_shape("Pacman_Left.gif")
wn.register_shape("Pacman_Right.gif")
#wn.register_shape("Pacman_Bottom.gif")
#wn.register_shape("Pacman_Up.gif")
wn.register_shape("apple.gif")


# class for the Maze turtle (white square)
class Maze(turtle.Turtle):               # define a Maze class
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("map.gif")
        self.penup()
        self.speed(0)

# class for the End Or Food (fruit)
class End(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("apple.gif")
        self.penup()
        self.speed(0) 

# class for the sprite pacman (yellow)
class Sprite(turtle.Turtle):  #turtle hareket eden nesne olarak baz alındı
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("Pacman_Right.gif")
        self.setheading(270)  # point turtle to point down
        #self.pen(fillcolor="black", pencolor="yellow", pensize=10)
        self.speed(0)
        self.travel_cost=0

    def spritedown(self):
        if (self.heading() == 270):                   #Pacman Yön Ayarı Yapılacak Left-Right
            x_walls = round(sprite.xcor(),0)          
            y_walls = round(sprite.ycor(),0)
            if (x_walls, y_walls) in finish:          
                print("Finished")
                endProgram()
            if (x_walls +24, y_walls) in walls:           
                Heuristic.TravelCost(self)
                if(x_walls, y_walls -24) not in walls:   
                    self.forward(24)
                else:
                    self.right(90)
            else:
                Heuristic.TravelCost(self)
                self.left(90)
                self.forward(24)

    def spriteright(self):
        if (self.heading() == 0):
            x_walls = round(sprite.xcor(),0)
            y_walls = round(sprite.ycor(),0)
            if (x_walls, y_walls) in finish:   # check turtle coordinates are at the finish line
                print("Finished")
                endProgram()
            if (x_walls, y_walls +24) in walls:       # check to see if they are walls on the left
                Heuristic.TravelCost(self)
                if(x_walls +24, y_walls) not in walls:
                    self.forward(24)
                else:
                    self.right(90)
            else:
                Heuristic.TravelCost(self)
                self.left(90)
                self.forward(24)

    def spriteup(self):
        if (self.heading() == 90):
            x_walls = round(sprite.xcor(),0)
            y_walls = round(sprite.ycor(),0)
            if (x_walls, y_walls) in finish:   # check turtle coordinates are at the finish line
                print("Finished")
                endProgram()
            if (x_walls -24, y_walls ) in walls:  # check to see if they are walls on the left
                Heuristic.TravelCost(self)
                if (x_walls, y_walls + 24) not in walls:
                    self.forward(24)
                else:
                    self.right(90)
            else:
                Heuristic.TravelCost(self)
                self.left(90)
                self.forward(24)

    def spriteleft(self):  
        if (self.heading() == 180):
            x_walls = round(sprite.xcor(),0)
            y_walls = round(sprite.ycor(),0)
            if (x_walls, y_walls) in finish:   # check turtle coordinates are at the finish line
                print("Finished")
                endProgram()
            if (x_walls, y_walls -24) in walls:  # check to see if they are walls on the left
                Heuristic.TravelCost(self)
                if (x_walls - 24, y_walls) not in walls:
                    self.forward(24)
                else:
                    self.right(90)
            else:
                Heuristic.TravelCost(self)
                self.left(90)
                self.forward(24)

def endProgram():
    wn.exitonclick()
    sys.exit()
pathDict={

}

def IsPosible(x_pos,y_pos):
    if (x_pos+24,y_pos) not in walls and (x_pos+24,y_pos) not in visited: #            xxP P Bir Duvarmı ? Veya P Ziyaret Edildi Mi?
        pathDict[(x_pos+24,y_pos)]=(x_pos,y_pos)
        queue.put((x_pos+24,y_pos))
        visited.append((x_pos+24,y_pos))
    if (x_pos-24,y_pos) not in walls and (x_pos-24,y_pos) not in visited:
        pathDict[(x_pos-24,y_pos)]=(x_pos,y_pos)
        queue.put((x_pos-24,y_pos))
        visited.append((x_pos-24,y_pos))
    if (x_pos,y_pos+24) not in walls and (x_pos,y_pos+24) not in visited:
        pathDict[(x_pos,y_pos+24)]=(x_pos,y_pos)
        queue.put((x_pos,y_pos+24))
        visited.append((x_pos,y_pos+24))
    if (x_pos,y_pos-24) not in walls and (x_pos,y_pos-24) not in visited:
        pathDict[(x_pos,y_pos-24)]=(x_pos,y_pos)
        queue.put((x_pos,y_pos-24))
        visited.append((x_pos,y_pos-24))
    if(len(queue.queue)!=0) and (-288.0,232.0) not in visited: #Test Cord end.xcor(),end.ycor()
        x_y_pos=queue.get()
        IsPosible(x_y_pos[0],x_y_pos[1])
    else:
        return
    

grid = [
#Grid İçinde Rastgele Bir Yere Elaman Eklenirken Bunu Grid Üzerinde Boş Olen Yerlerden Birine Yapıcaz.
"++++++++++++++++++++++++++++++++++++++++", #40x21
"+s               +++++++e              +",
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

backtraverse_paths=[] #Rekürsif Fonksiyonun İçinden Değer Çıkarmak İçin Global Değişken Dışında Daha Doğru ?
def BackTraverse(corx,cory):
    backtraverse_paths.append((corx,cory))
    last_path=pathDict[(corx,cory)]
    if  last_path != (-456.0,232.0):
        BackTraverse(last_path[0],last_path[1])
    else:
        backtraverse_paths.append((corx,cory))
        return


def setupMaze(grid):
    for y in range(len(grid)):                       # select each line in the grid   Labirent İçin Kodlanan Grid'in Tüm Birimleri Çizilecek
        for x in range(len(grid[y])):                # identify each character in the line
            character = grid[y][x]                   
            screen_x = ((-res_x/2)+(res_x-960)/2) + (x * 24)   #Her Bir Square 24x24 Bit       960=40*24
            screen_y = (res_y/3) - (y * 24)    #Ekrandaki Maze Tam Center'lı Gibi Düşünülmeli Analitik Düzlem Üzerinde 

            if character == "+":                     # if grid character contains an +
                maze.goto(screen_x, screen_y)        # move turtle to the x and y location and
                maze.stamp()                         # stamp a copy of the turtle (white square) on the screen
                walls.append((screen_x, screen_y))   # add coordinate to walls list

            if character == "e":                     # if grid character contains an e
                end.goto(screen_x, screen_y)         # move turtle to the x and y location and
                end.stamp()                          # stamp a copy of the turtle (green square) on the screen
                finish.append((screen_x, screen_y))  # add coordinate to finish list

            if character == "s":                     # if the grid character contains an s
                sprite.goto(screen_x, screen_y)      # move turtle to the x and y location
                sprite.pen(fillcolor="black", pencolor="yellow", pensize=10)

# ############ main program starts here  ######################

maze = Maze()                # enable the maze class
sprite = Sprite()            # enable the sprite  class
end = End()                  # enable End position class
walls =[]                    # create walls coordinate list
finish = []                  # enable the finish array

setupMaze(grid)              # call the setup maze function

visited.append((sprite.xcor(),sprite.ycor()))  #İlk Değeri Visited Olarak İşaretlendi              
IsPosible(sprite.xcor(),sprite.ycor()) #

BackTraverse(-288.0,232.0)
print(backtraverse_paths)

while True:
    sprite.spriteright()
    sprite.spritedown()
    sprite.spriteleft()
    sprite.spriteup() 
    time.sleep(1)

