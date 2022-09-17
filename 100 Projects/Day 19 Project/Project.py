from turtle import Turtle, Screen

donatello = Turtle(shape = "turtle")
donatello.penup()
donatello.color("purple")

leonardo = Turtle(shape = "turtle")
leonardo.penup()
leonardo.color("blue")

michelangelo = Turtle(shape = "turtle")
michelangelo.penup()
michelangelo.color("orange")

raphael = Turtle(shape = "turtle")
raphael.penup()
raphael.color("red")

colors = ["purple", "blue", "orange", "red"]
y_positions = [150, 50, -50, -150]
turtles = []

screen = Screen()
screen.setup(width = 500, height = 450)
user_bet = screen.textinput(title = "Make your bet", prompt = "Choose between \"Donatello\", \"Leonardo\", \"Michelangelo\", \"Raphael\"\nEnter your choice: ").lower()

for turtle_index in range(4):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x = -235, y = y_positions[turtle_index])
    turtles.append(new_turtle)

screen.exitonclick()