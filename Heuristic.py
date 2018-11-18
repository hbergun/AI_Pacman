import math
def ManhattanDistance(sprite_x,sprite_y,target_x,target_y):
    distance_x=target_x-sprite_x
    distance_y=target_y-sprite_y
    return abs(distance_x)+abs(distance_y)

def TwoDotDiff(sprite_x,sprite_y,target_x,target_y):
     return math.sqrt(pow((target_x-sprite_x),2)+pow((target_y-sprite_y),2))

def TravelCost(self):
     self.travel_cost+=24
     print("Gezinme Maliyeti",self.travel_cost)
          