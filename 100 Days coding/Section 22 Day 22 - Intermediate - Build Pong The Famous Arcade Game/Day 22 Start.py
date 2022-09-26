from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.tracer(0)
screen.bgcolor('black')
screen.title('Ping Pong')
screen.setup(width=800, height=600)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

ball = Ball()

while True:
    screen.update()
    ball.move_ball()
    ball.collision_with_wall()
    time.sleep(0.07)

screen.exitonclick()