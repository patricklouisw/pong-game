from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def increment_left(self):
        self.l_score += 1
        self.write_score()

    def increment_right(self):
        self.r_score += 1
        self.write_score()

    def reset(self):
        self.l_score = 0
        self.r_score = 0
        self.write_score()
