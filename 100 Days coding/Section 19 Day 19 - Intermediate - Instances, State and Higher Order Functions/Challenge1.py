from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()

def move_forward():
    tom.forward(10)

def move_backward():
    tom.bakcward(10)

screen.listen()
screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_backward)
screen.exitonclick()