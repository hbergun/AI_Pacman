import turtle
import math
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Pacman Game With Artificial Intelligence")
wn.setup(700,700)
 


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
        
class player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("Pacman_Right.gif")
        self.color("yellow")
        self.penup()
        self.speed(0)
    
    def go_up(self):
        #bir sonraki hamlenin koordinatları alınıyor
        move_to_x=player.xcor()
        move_to_y=player.ycor()+24
        #eğer bir sonraki hamle duvar değilse oyna
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y) 
            self.shape("Pacman_Up.gif")
    
    def go_down(self):
        move_to_x=player.xcor()
        move_to_y=player.ycor()-24
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
            self.shape("Pacman_Bottom.gif")
           
            
    
    def go_left(self):
         move_to_x=player.xcor()-24
         move_to_y=player.ycor()
         if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
            self.shape("Pacman_Left.gif")
    
    def go_right(self):
         move_to_x=player.xcor()+24
         move_to_y=player.ycor()
         if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
            self.shape("Pacman_Right.gif")
            
    def is_collision(self, other):
        a=self.xcor()-other.xcor()
        b=self.ycor()-other.ycor()
        distance = math.sqrt((a**2) + (b**2))
        if distance < 5:
            return True
        else:
            return False
        
class forage(turtle.Turtle):
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
            screen_x = -588 + (x * 24)   #Her Bir Square 24x24 Bit       
            screen_y = 288 - (y * 24)    #Ekrandaki Maze Tam Center'lı Gibi Düşünülmeli Analitik Düzlem Üzerinde             

            if character == "+":                     
                maze.goto(screen_x, screen_y)        
                maze.stamp()   #Elemanın Ekranda Kalmasını Sağlıyor Stampleniyor                      
                walls.append((screen_x, screen_y))   
            elif character =="P":
                player.goto(screen_x, screen_y)        
            elif character=="T":
                forages.append(forage(screen_x,screen_y))    
            
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
player=player()


walls=[]  #oyun duvarları koordinatları
forages=[]
create_maze(grid)

#print(walls) eğer koordinatları görmek istiyorsanız
turtle.listen()

turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_down,"Down")
turtle.onkey(player.go_up,"Up")
wn.tracer(0)

while True:
    for forage in forages:
        if player.is_collision(forage): 
            forage.destroy()
            forages.remove(forage)
 
    #Ekranı Günceller
    wn.update()    

