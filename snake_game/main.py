from turtle import Turtle, Screen
import time
from Snake_program import Snake
from Screen_program import SnakeScreen
from food import Food
from scoreboard import Scoreboard

object_name_list = ["snk_1","snk_2","snk_3"]

snake = Snake()
snake_screen = SnakeScreen()
screen = Screen()
food = Food()
scoreboard = Scoreboard()



game_ison = True

while game_ison:
    for segments in snake.object_list[1:]:
        if segments.distance(snake.object_list[0])<10:
            game_ison = False
            scoreboard.gameover()
    #collision detection with food 
    if snake.object_list[0].distance(food) < 15:
       food.refersh() 
       scoreboard.increase_score()
       snake.extend()

    snake.move()
    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right,"Right")


    

screen.exitonclick()

