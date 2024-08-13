from turtle import Turtle, Screen
import time

screen = Screen()

NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180


class Snake:
    def __init__(self) :
        self.object_name_list = ["snk_1","snk_2","snk_3","snk_4"]
        self.object_name_count = 5
        self.object_list = []
        self.x_value = 0
        for object in self.object_name_list:
            self.snake_creation(object,x_cor=self.x_value,y_cor=0)
            self.x_value-=20

    def snake_creation(self,object,x_cor,y_cor):
        object = Turtle()
        object.shape("square")
        object.color("White")
        object.penup()
        object.goto(x_cor,y_cor)
        self.object_list.append(object)
        return object

    def extend(self): 
        self.object_name =f"snk_{self.object_name_count}" 
        self.object_name_list.append(self.object_name)       
        object =self.snake_creation(self.object_name_list[-1],x_cor=self.x_value,y_cor=0)
        self.object_list.append(object)
        self.object_name_count +=1

    def move(self):
        time.sleep(0.1)
        for num in range(len(self.object_list)-1,0,-1):
                new_x = self.object_list[num-1].xcor()
                new_y = self.object_list[num-1].ycor()
                self.object_list[num].goto(new_x,new_y) 
                
        self.object_list[0].forward(20)
        if self.object_list[0].xcor()>300:
            self.object_list[0].goto(-300,self.object_list[0].ycor())
        if self.object_list[0].xcor()< -300:
            self.object_list[0].goto(300,self.object_list[0].ycor())
        if self.object_list[0].ycor()>300:
            self.object_list[0].goto(self.object_list[0].xcor(),-300)
        if self.object_list[0].ycor()< -300:
            self.object_list[0].goto(self.object_list[0].xcor(),300)
        
        screen.update() 

    def up(self):
         if self.object_list[0].heading()!=SOUTH:
            self.object_list[0].setheading(NORTH)
    def down(self):
         if self.object_list[0].heading()!=NORTH:
            self.object_list[0].setheading(SOUTH)
    def left(self):
         if self.object_list[0].heading()!=EAST:
            self.object_list[0].setheading(WEST)
    def right(self):
         if self.object_list[0].heading()!=WEST:
            self.object_list[0].setheading(EAST)