from turtle import Turtle, Screen

tom = Turtle()
# tom.shape("turtle")
tom.color("midnight blue")
for _ in range(10):
    tom.pendown()
    tom.forward(10)
    tom.penup()
    tom.forward(10)

screen_time = Screen()
screen_time.exitonclick()