from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,postion) :
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1,stretch_wid=4)
        self.color("white")
        self.penup()
        self.goto(postion)

    def move_up(self):
        self.new_y = self.ycor()+20
        self.goto(x=self.xcor(),y=self.new_y)
        

    def move_down(self):
        self.new_y = self.ycor()-20
        self.goto(x=self.xcor(),y=self.new_y)

