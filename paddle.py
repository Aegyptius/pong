from turtle import Turtle

STRETCH_WIDTH = 5
STRETCH_LENGTH = 1
X_POSITION = 350
Y_POSITION = 0

class Paddle:
    def __init__(self):
        self.paddle = Turtle()
        self.paddle.color("white")
        self.paddle.shape("square")
        self.paddle.speed("fastest")
        self.paddle.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_LENGTH)
        self.paddle.penup()
        self.paddle.goto(X_POSITION, Y_POSITION)
