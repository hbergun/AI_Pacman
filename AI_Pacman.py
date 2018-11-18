import turtle
import math
import tkinter
import ctypes
import Heuristic
import queue
queue=queue.Queue()
res_x=ctypes.windll.user32.GetSystemMetrics(0)
res_y=ctypes.windll.user32.GetSystemMetrics(1)
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Pacman Game With Artificial Intelligence")
wn.setup(width=.99,height=.90,startx=0,starty=0)
 
#register shapes
wn.register_shape("map.gif")
wn.register_shape("apple.gif")
wn.register_shape("Pacman_Right.gif")
wn.register_shape("Pacman_Left.gif")
wn.register_shape("Pacman_Bottom.gif")
wn.register_shape("Pacman_Up.gif")

#maze yarat
class Maze(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("map.gif")
        self.pen(fillcolor="black", pencolor="yellow", pensize=10)
        self.penup()
        self.speed(0)
        
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("Pacman_Right.gif")
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.travel_cost=0
    
    def go_up(self):
        #bir sonraki hamlenin koordinatları alınıyor
        move_to_x=player.xcor()
        move_to_y=player.ycor()+24
        #eğer bir sonraki hamle duvar değilse oyna
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
            self.shape("Pacman_Up.gif")
            Heuristic.TravelCost(self)
    
    def go_down(self):
        move_to_x=player.xcor()
        move_to_y=player.ycor()-24
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
            self.shape("Pacman_Bottom.gif")
            Heuristic.TravelCost(self)
           
    
    def go_left(self):
         move_to_x=player.xcor()-24
         move_to_y=player.ycor()
         if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
            self.shape("Pacman_Left.gif")
            Heuristic.TravelCost(self)

    
    def go_right(self):
         move_to_x=player.xcor()+24
         move_to_y=player.ycor()
         if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
            self.shape("Pacman_Right.gif")
            Heuristic.TravelCost(self)


            
    def is_collision(self, other):
        a=self.xcor()-other.xcor()
        b=self.ycor()-other.ycor()
        distance = math.sqrt((a**2) + (b**2))
        if distance < 5:
            return True
        else:
            return False
        
class Forage(turtle.Turtle):
    def __init__(self,x,y): #Yem kurucu metod
        turtle.Turtle.__init__(self)
        self.shape("apple.gif")
        self.color("red")
        self.penup()
        self.speed(0) 
        self.goto(x,y)
    
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle() 


def create_maze(grid):
    for y in range(len(grid)):                      #Labirent İçin Kodlanan Grid'in Tüm Birimleri Çizilecek
        for x in range(len(grid[y])):                
            character = grid[y][x]                   
            screen_x = ((-res_x/2)+(res_x-960)/2) + (x * 24)   #Her Bir Square 24x24 Bit       960=40*24
            screen_y = (res_y/3) - (y * 24)    #Ekrandaki Maze Tam Center'lı Gibi Düşünülmeli Analitik Düzlem Üzerinde             

            if character == "+":                     
                maze.goto(screen_x, screen_y)        
                maze.stamp()   #Elemanın Ekranda Kalmasını Sağlıyor Stampleniyor                      
                walls.append((screen_x, screen_y))   
            elif character == "P": #Hadi Bu Pacman 'in P si
                player.goto(screen_x, screen_y)

                print('Pacman ',screen_x,screen_y)        
            elif character == "T": # T yi koyarken neyi düşündün ??
                forages.append(Forage(screen_x,screen_y))
                print("Forage",screen_x,screen_y)    
            
grid = [
#Grid İçinde Rastgele Bir Yere Elaman Eklenirken Bunu Grid Üzerinde Boş Olen Yerlerden Birine Yapıcaz.
"++++++++++++++++++++++++++++++++++++++++", #40x21
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
player=Player()
walls=[]  #oyun duvarları koordinatları
forages=[]
create_maze(grid)

#print(walls) eğer koordinatları görmek istiyorsanız
wn.listen()

wn.onkey(player.go_left,"Left")
wn.onkey(player.go_right,"Right")
wn.onkey(player.go_down,"Down")
wn.onkey(player.go_up,"Up")

wn.tracer(0)

while True:
    for forage in forages:
        if player.is_collision(forage): 
            forage.destroy()
            forages.remove(forage)
 
    #Ekranı Günceller
    wn.update()    

