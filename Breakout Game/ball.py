from turtle import Turtle, Screen
import random as rd
import sys
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.health=3
        self.create_ball()
        
        
    def increase_speed(self,speed):
        self.speed = speed
        if self.speed >0:
            self.speed+=1
        else:
            self.speed-=1
            
    def create_ball(self):
        self.pendown()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.penup()
        self.move_y = -15
        num = [-15,15]
        self.move_x = rd.choice(num)
        self.goto(x=0,y=-50)
        self.setheading(270)
        
    def hit_wall(self):
        self.pendown()
        self.move_x *=-1 
        
    def hit_up(self):
        self.pendown()
        self.increase_speed(self.move_y)
        self.move_y *=-1 



    def hit_bricks(self):
        self.pendown()
        self.increase_speed(self.move_y)
            
        self.move_y *= -1
        
        
    def ball_moving(self):
        try:
            current_x =int(self.xcor())
            current_y = int(self.ycor())
            
            next_x = current_x + self.move_x
            next_y = current_y + self.move_y
            
            self.penup()
            self.goto(x=next_x,y=next_y)
        except:
            sys.exit(1)
        
    def hit_paddle(self):
        self.pendown()
        self.move_y *= -1

    def game_ovar(self):
        self.penup()
        self.goto(x=2000,y=2000)
        self.clear()
        self.create_ball()
