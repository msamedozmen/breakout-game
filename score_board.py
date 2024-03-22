from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        self.score=0
        self.high= 0
        self.color("white")
        self.penup()
        self.goto(0,340)
        self.hideturtle()
        self.write(f" Score: {self.score}    High Score: {self.high} ", True, align="center",font=("Arial",20,"normal"))
        
        
    def score_up(self):
        self.score +=1
        self.clear()
        self.penup()
        self.goto(0,340)
        self.write(f" Score: {self.score}    High Score: {self.high} ", True, align="center",font=("Arial",20,"normal"))
        
        
    def reset_score_board(self):
        if self.score > self.high:
            self.high = self.score
            self.score = 0
        self.score =0
        self.clear()
        self.color("white")
        self.penup()
        self.goto(0,340)
        self.hideturtle()
        self.write(f" Score: {self.score}    High Score: {self.high} ", True, align="center",font=("Arial",20,"normal"))
