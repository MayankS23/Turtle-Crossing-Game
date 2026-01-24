from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, xcor):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(xcor, 200)
        self.write(self.l_score, align="center", font=("courier", 80, "normal"))

    def increase_score(self, score):
        self.clear()
        self.write(score, align="center", font=("courier", 80, "normal"))
