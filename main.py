from turtle import Turtle, Screen
from paddle import Paddle

SCREENWIDTH = 800
SCREENHEIGHT = 600

screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREENWIDTH, height=SCREENHEIGHT)
screen.title("Pong")

paddle_right = Paddle()

screen.listen()
screen.onkey(fun=paddle_right.paddle_up(), key="Up")



screen.exitonclick()