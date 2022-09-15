from turtle import Turtle, Screen

tom = Turtle()
tom.shape("turtle")
tom.color("midnight blue")
for _ in range(0, 4):
    tom.right(90)
    tom.forward(100)

screen_time = Screen()
screen_time.exitonclick()