from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.tracer(0)
screen.bgcolor('black')
screen.title('Pong')
screen.setup(width=800, height=600)

scoreboard = ScoreBoard()

right_paddle = Paddle((370, 0))
left_paddle = Paddle((-370, 0))

screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

ball = Ball()

while True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Detect collision with wall
    if -280 > ball.ycor() or ball.ycor() > 280:
        ball.y_bounce()
    #Detect collision with paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 345) or (ball.distance(left_paddle) < 50 and ball.xcor() < -345):
        ball.x_bounce()
    #Detect when the R paddle misses
    if ball.xcor() > 420:
        scoreboard.l_point()
        ball.reset()
    #Detect when the R paddle misses
    if ball.xcor() < -420:
        scoreboard.r_point()
        ball.reset()