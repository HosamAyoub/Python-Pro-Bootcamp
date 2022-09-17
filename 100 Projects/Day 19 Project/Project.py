from turtle import Turtle, Screen

tom = Turtle()
tom.shape("turtle")
tom.penup()
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Choose between \"Donatello\", \"Leonardo\", \"Michelangelo\", \"Raphael\"\nEnter your choice: ").lower()
tom.goto(x = -235, y = -100)

screen.exitonclick()