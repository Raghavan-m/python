from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.y_incrementor = 10
        self.x_incrementor = 10
        self.ball_speed = 0.1
    
    def move(self):
        new_x =self.xcor()+self.x_incrementor
        new_y =self.ycor()+self.y_incrementor
        self.goto(new_x,new_y)

    def bounce_wall(self):
        self.y_incrementor *=-1 

    def bounce_paddle(self):
        self.x_incrementor *=-1 
        self.ball_speed *=0.9
