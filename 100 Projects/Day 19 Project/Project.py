from turtle import Turtle, Screen

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