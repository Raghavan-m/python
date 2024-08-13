from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,280)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"Scoreboard: {self.score}",False,"center",("Arial",14,"bold"))

    def gameover(self):
        self.goto(0,0)
        self.write(f"GAME OVER ",False,"center",("Arial",24,"bold"))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()