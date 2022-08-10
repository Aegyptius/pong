from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

SCREENWIDTH = 800
SCREENHEIGHT = 600
distance_x = 10
distance_y = 10

screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREENWIDTH, height=SCREENHEIGHT)
screen.title("Pong")
# Tracer method controls the animation. 0 turns off the animation completely
# Must manually update in order to see object
screen.tracer(0)

paddle_right = Paddle()
paddle_left = Paddle(-350)
ball = Ball()

screen.listen()
# NOTE: Do not use parentheses when passing function as a parameter
screen.onkey(fun=paddle_right.paddle_up, key="Up")
screen.onkey(fun=paddle_right.paddle_down, key="Down")
screen.onkey(fun=paddle_left.paddle_up, key="w")
screen.onkey(fun=paddle_left.paddle_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move(distance_x, distance_y)
    if ball.ycor() >= 280:
        distance_y *= -1
    elif ball.ycor() <= -280:
        distance_y *= -1

screen.exitonclick()
