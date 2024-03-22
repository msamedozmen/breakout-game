from turtle import Turtle
import random as rd


rows= [x for x in range(-370,401,61)]

columns = [y for y in range(90,270,22)]

colors = ["green","yellow","red"]

class Bricks(Turtle):
    def __init__(self):
        super().__init__()
        self.brick_list = []
        self.speed("fastest")
        self.create_bricks()
            
    def create_bricks(self):
        for column in columns:
            for row in rows:
                self.brick = Turtle()
                self.brick.shape("square")
                self.brick.shapesize(stretch_wid=1,stretch_len=2.95)
                color = rd.choice(colors)
                self.brick.color("white")
                self.brick.penup()
                self.brick.goto(x=row,y=column)
                self.brick_list.append(self.brick)



    def remmove_bricks(self,brick):
        self.deleted_brick =brick
        self.brick_list.remove(brick)
        
    
    
    def reset_game(self):
        self.brick_list.clear()
        self.speed("fastest")
        self.create_bricks()
    