from turtle import Turtle, Screen

class SnakeScreen:
    def __init__(self) :
        
        screen =  Screen()
        screen.bgcolor("black")
        screen.title("snake game")
        screen.setup(height=600,width=600)
        screen.tracer(0)