from turtle import Turtle

class ScoreBoard_right(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(30,250)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
         self.write(f"{self.score}",False,align="center",font=("arial",20,"bold"))

    def score_increase(self):
        self.clear()
        self.score+=1
        self.update_scoreboard()

class ScoreBoard_left(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-30,250)
        self.color("white")
        self.update_scoreboard()
        

    def update_scoreboard(self):
         self.write(f"{self.score}",False,align="center",font=("arial",20,"bold"))

    def score_increase(self):
            self.clear()
            self.score+=1
            self.update_scoreboard()





