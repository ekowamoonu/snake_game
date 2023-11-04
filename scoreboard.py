import turtle
from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.initial_score = 0
        self.write(f"Score: {self.initial_score}", align="center", font=("Arial", 17, "bold"))
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("OUCH!! GAME OVER", align="center", font=("Impact", 25, "bold"))

    def refresh(self):
        self.initial_score += 1
        self.clear()
        self.write(f"Score: {self.initial_score}", align="center", font=("Arial", 17, "bold"))
