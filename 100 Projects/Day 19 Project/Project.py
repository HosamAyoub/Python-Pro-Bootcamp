from turtle import Turtle, Screen

donatello = Turtle(shape = "turtle")
donatello.penup()

leonardo = Turtle(shape = "turtle")
leonardo.penup()

michelangelo = Turtle(shape = "turtle")
michelangelo.penup()

raphael = Turtle(shape = "turtle")
raphael.penup()

screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Choose between \"Donatello\", \"Leonardo\", \"Michelangelo\", \"Raphael\"\nEnter your choice: ").lower()

donatello.goto(x = -235, y = 150)
leonardo.goto(x = -235, y = 50)
michelangelo.goto(x = -235, y = -50)
raphael.goto(x = -235, y = -150)

screen.exitonclick()