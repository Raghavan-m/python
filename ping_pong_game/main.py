# from pong_screen import ScreenClass
from paddle import Paddle
from turtle import Screen
from ball import Ball
from ScoreBoard import ScoreBoard_right,ScoreBoard_left
import time 

score_left = 0
score_right = 0

ball = Ball()
game_ison = True

screen = Screen()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("Ping Pong game")



screen.tracer(0)
r_paddele = Paddle((380, 0))
l_paddele = Paddle((-380, 0))


screen.listen()

screen.onkey(r_paddele.move_up, "Up")
screen.onkey(r_paddele.move_down, "Down")


screen.onkey(l_paddele.move_up, "w")
screen.onkey(l_paddele.move_down, "s")

scoreboard_right = ScoreBoard_right()
scoreboard_left = ScoreBoard_left()

while game_ison:
    time.sleep(ball.ball_speed)
    screen.update()
    
    ball.move()
    
    if ball.ycor() > 280 : 
        ball.bounce_wall()

    if ball.ycor() < -280 : 
        ball.bounce_wall()

    if (ball.distance(r_paddele) < 60 and ball.xcor()>360) or (ball.distance(l_paddele) <50 and ball.xcor()< -360):
        ball.bounce_paddle()
    
    elif ball.xcor()>360:
        scoreboard_left.score_increase()
        ball.goto(0,0)
        ball.bounce_paddle()
        ball.ball_speed = 0.1
    
    elif ball.xcor()< -360:
        scoreboard_right.score_increase()
        ball.goto(0,0)
        ball.bounce_paddle()
        ball.ball_speed = 0.1

        


screen.exitonclick()
