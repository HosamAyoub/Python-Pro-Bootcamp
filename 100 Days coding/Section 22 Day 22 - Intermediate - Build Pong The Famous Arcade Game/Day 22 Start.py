from turtle import Screen


screen = Screen()
screen.tracer(0)
screen.bgcolor('black')
screen.title('Ping Pong')
screen.setup(width=800, height=600)



screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")