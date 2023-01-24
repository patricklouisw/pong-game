import random
from turtle import Turtle

HALF_TURTLE_SIZE = 10
BALL_SIZE = 1

class Ball(Turtle):
    def __init__(self, max_width:int, max_height):
        super().__init__()
        self.max_width = max_width
        self.min_width =  -max_width
        self.max_height = max_height
        self.min_height = -max_height
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_len=BALL_SIZE, stretch_wid=BALL_SIZE)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1

    def pad_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_move *= -1
