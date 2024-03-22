from turtle import Turtle, Screen



class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.create_paddle()
        self.speed("fastest")

    
    def create_paddle(self):
        self.pendown()

        self.shape("square")
        self.color("gray")
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.penup()
        self.goto(x=0,y=-270)
        
        
    def move_left(self):
        self.pendown()
        current_x = self.xcor()
        current_y = self.ycor()
        x = current_x - 35
        self.penup()
        self.goto(x=x,y=current_y)
        
        
    def move_right(self):
        self.pendown()

        current_x = self.xcor()
        current_y = self.ycor()
        
        x= current_x +35
        self.penup()
        self.goto(x=x,y=current_y)
        
        
    def game_over(self):
        self.penup()
        self.clear()
        self.speed("fastest")
        self.create_paddle()