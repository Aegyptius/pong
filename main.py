from turtle import Turtle, Screen
from paddle import Paddle

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


screen.listen()
#NOTE: Do not use parentheses when passing function as a parameter
screen.onkey(fun=paddle_right.paddle_up, key="Up")
screen.onkey(fun=paddle_right.paddle_down, key="Down")
screen.onkey(fun=paddle_left.paddle_up, key="w")
screen.onkey(fun=paddle_left.paddle_down, key="s")

game_is_on = True
while game_is_on:
    screen.update()






screen.exitonclick()