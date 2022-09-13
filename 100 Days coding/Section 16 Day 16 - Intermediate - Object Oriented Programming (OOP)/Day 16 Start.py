from turtle import Turtle, Screen
import prettytable

tom = Turtle()
tom.shape("turtle")
tom.color("dark blue")
tom.forward(100)
print(tom)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
