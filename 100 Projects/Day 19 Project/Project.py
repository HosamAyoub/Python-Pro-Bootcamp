from turtle import Turtle, Screen
from random import randint

colors = ["purple", "blue", "orange", "red"]
y_positions = [150, 50, -50, -150]
turtles = []
turtles_names = ["donatello", "leonardo", "michelangelo", "raphael"]
screen = Screen()
screen.setup(width = 500, height = 450)
user_bet = ""

while user_bet not in turtles_names:
    user_bet = screen.textinput(title = "Make your bet", prompt = "Choose between \"Donatello\", \"Leonardo\", \"Michelangelo\", \"Raphael\"\nEnter your choice: ").lower()

for turtle_index in range(4):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x = -235, y = y_positions[turtle_index])
    turtles.append(new_turtle)
    print(id(new_turtle))

race_on = True
while race_on:
    for turtle in turtles:
        turtle.forward(randint(0, 10))
        if turtle.xcor() >= 235:
            if turtles.index(turtle) == turtles_names.index(user_bet):
                print(f"You've won! the {user_bet.capitalize()} turtle is the winner!")
            else:
                print(f"You've lost! the {turtles_names[turtles.index(turtle)].capitalize()} turtle is the winner!")
            race_on = False
            break