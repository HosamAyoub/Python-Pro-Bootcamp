from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()

def move_forward():
    tom.forward(10)

def move_backward():
    tom.backward(10)

def rotate_clock_wise():
    tom.right(10)
    
def rotate_counter_clock_wise():
    tom.left(10)

def clear():
    tom.clear()
    tom.home()

screen.listen()
screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_backward)
screen.onkey(key = "d", fun = rotate_clock_wise)
screen.onkey(key = "a", fun = rotate_counter_clock_wise)
screen.onkey(key = "c", fun = clear)
screen.exitonclick()