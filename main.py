from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from score_board import ScoreBoard
import random 
import time


my_screen = Screen()
my_screen.setup(width=800,height=800)
my_screen.bgcolor("black")
my_screen.title("Break Out")
my_screen.tracer(0.1)
my_screen.bgpic("ezgif.com-gif-maker.gif")


ball = Ball()
paddle = Paddle()
bricks = Bricks()
score =ScoreBoard()

my_screen.onkey(key="Left",fun=paddle.move_left)
my_screen.onkey(key="Right",fun=paddle.move_right)
my_screen.listen()
is_game = True

while is_game:
    my_screen.update()
    time.sleep(0.1)
    ball.ball_moving()
    if paddle.distance(ball)<55 and ball.ycor()<-250:
        ball.hit_bricks()
        
    if ball.xcor()>400 or ball.xcor()<-400:
        ball.hit_wall()
        
    if ball.ycor()>300:
        ball.hit_up()
        
        
    for brick in bricks.brick_list:
        if ball.distance(brick)<40:
            if abs(bricks.xcor() - ball.xcor())< 20:
                brick.hideturtle()
                brick.goto(x=2000,y=2000)
                ball.hit_wall()
                score.score_up()
            else:
                brick.hideturtle()
                brick.goto(x=2000,y=2000)
                ball.hit_up()       
                score.score_up() 
            
    if ball.ycor()<-290:
        ball.game_ovar()
        bricks.reset_game()
        score.reset_score_board()
    
my_screen.exitonclick()