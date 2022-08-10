from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("slowest")
        self.penup()
        self.goto(0, 0)

    def move(self, distance_x, distance_y):
        self.goto(self.xcor() + distance_x, self.ycor() + distance_y)

