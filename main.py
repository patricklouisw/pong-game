from turtle import Screen
from ball import Ball
from pad import Pad
from scoreboard import Scoreboard
import time

PADDING = 50
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MAX_WIDTH = SCREEN_WIDTH // 2
MIN_WIDTH = -MAX_WIDTH
MAX_HEIGHT = SCREEN_HEIGHT // 2
MIN_HEIGHT = -MAX_HEIGHT

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("Pong!")
screen.bgcolor("black")
screen.tracer(0)

pad1 = Pad(MIN_WIDTH + PADDING, 0)
pad2 = Pad(MAX_WIDTH - PADDING, 0)
ball = Ball(MAX_WIDTH, MAX_HEIGHT)
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="w", fun=pad1.up)
screen.onkey(key="s", fun=pad1.down)
screen.onkey(key="Up", fun=pad2.up)
screen.onkey(key="Down", fun=pad2.down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # If ball hits the wall
    if ball.ycor() > 280 or \
            ball.ycor() < -280:
        ball.wall_bounce()

    # If ball hits the pad
    if (ball.distance(pad2) < 50 and ball.xcor() > 320) or \
            (pad1.distance(ball) < 50 and ball.xcor() < -320):
        ball.pad_bounce()

    # If ball hits the goal
    if ball.xcor() > MAX_WIDTH:
        scoreboard.increment_left()
        ball.reset()
    elif ball.xcor() < MIN_WIDTH:
        scoreboard.increment_right()
        ball.reset()





screen.exitonclick()
