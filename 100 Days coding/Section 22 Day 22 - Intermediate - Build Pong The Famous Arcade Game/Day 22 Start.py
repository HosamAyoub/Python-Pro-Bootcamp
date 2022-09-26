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
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

ball = Ball()

while True:
    time.sleep(0.09)
    screen.update()
    ball.move()
    #Detect collision with wall
    if -280 > ball.ycor() or ball.ycor() > 280:
        ball.y_bounce()
    #Detect collision with paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 325) or (ball.distance(left_paddle) < 50 and ball.xcor() < -325):
        ball.x_bounce()
    #Detect when the paddle misses
    if ball.xcor() > 420 or ball.xcor() < -420:
        ball.reset()

screen.exitonclick()