from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

SCREENWIDTH = 800
SCREENHEIGHT = 600

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
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #if ball.xcor() > 380 or ball.xcor() < -380:
    #    ball.goto(0, 0)
    #    ball.bounce_x()
    #    time.sleep(1)

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()

screen.exitonclick()
