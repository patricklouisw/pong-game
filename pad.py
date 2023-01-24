from turtle import Turtle, tracer, update

HALF_TURTLE_SIZE = 10
PAD_WIDTH = 5
PAD_HEIGHT = 1
PAD_SPEED = 20


class Pad(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=PAD_HEIGHT, stretch_wid=PAD_WIDTH)
        self.goto(x, y)

    def up(self):
        new_x = self.xcor()
        new_y = self.ycor() + 20
        self.goto(new_x, new_y)

    def down(self):
        new_x = self.xcor()
        new_y = self.ycor() - 20
        self.goto(new_x, new_y)
