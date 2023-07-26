from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.create_paddle()

    def create_paddle(self):
        self.turtle
        self.penup()
        self.color("white")
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(self.position)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)
