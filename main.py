import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("pink")
screen.title("PONG")
screen.tracer(0)
score = Score()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()


screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down,"s")
a = 0.005
while True:
    time.sleep(a)
    ball.move()
    screen.update()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if ball.distance(r_paddle) <= 51 and ball.xcor() >= 330 or ball.distance(l_paddle) <=51 and ball.xcor() <= -330:
        ball.bounce_x()
        if a > 0.001:
            a -= 0.001 / 2

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
        a = 0.005


    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
        a = 0.005














screen.exitonclick()
