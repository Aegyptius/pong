from turtle import Turtle

STRETCH_WIDTH = 5
STRETCH_LENGTH = 1

class Paddle:
    #NOTE: To give a class parameter a default value, assign it in the init method parameters
    def __init__(self, starting_x=350, starting_y=0):
        self.paddle = Turtle()
        self.paddle.color("white")
        self.paddle.shape("square")
        self.paddle.speed("fastest")
        self.paddle.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_LENGTH)
        self.paddle.penup()
        self.paddle.goto(starting_x, starting_y)


    def paddle_up(self):
        if self.paddle.ycor() >= 240:
            pass
        else:
            self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() + 20)


    def paddle_down(self):
        if self.paddle.ycor() <= -240:
            pass
        else:
            self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() - 20)
