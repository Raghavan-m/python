from turtle import Turtle, Screen
import random
turtle_list = ["tim","tom","jerry","goku","vegeta"]
color_list = ["green","grey","orange","yellow","purple"]
count = 0 
object_list = []
start_y=-60
game_on = False
colors = ""
def create_turtle_set_color(object,color):
    object = Turtle()
    object.color(color)
    object.shape("turtle")
    return object

def go_to(object,x,y):
    object.penup()
    object.goto(x,y)

screen = Screen()
screen.setup(height=400,width=500)

for color in color_list:
    colors+=color+", "

user_bet = screen.textinput(title="make your Bet", prompt=f"Which colour turtle you want to bet({colors})!: ")
user_bet = user_bet.lower()
if user_bet:
    game_on = True

for name in turtle_list:
    name  = create_turtle_set_color(name,color_list[count])
    object_list.append(name)
    count+=1

for objects in object_list:
    go_to(objects,x=-230,y=start_y)
    start_y+=30

while game_on:
    for turtle in object_list:
        if turtle.xcor() > 230:
            game_on = False
            print(f"{turtle.pencolor()} color turtle  won the race")
            if user_bet == turtle.pencolor():
                print("you won")
            else:
                print(f"You loosse {turtle.pencolor()} won")
        movement = random.randint(0,10)
        turtle.forward(movement)

screen.exitonclick()