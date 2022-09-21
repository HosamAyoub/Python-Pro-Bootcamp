from turtle import Turtle

X_STARTING_POSITIONS = [0, -20, -40]

class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
    
    
    def create_snake(self):
        for x_pos in X_STARTING_POSITIONS:
            new_turtle = Turtle(shape='square')
            new_turtle.penup()
            new_turtle.color('white')
            new_turtle.goto(x=x_pos, y=0)
            self.turtles.append(new_turtle)


    def move(self):
        for turtle in range(len(self.turtles) - 1, 0, -1):
            new_pos = (self.turtles[turtle - 1].position())
            self.turtles[turtle].goto(new_pos)
        self.turtles[0].forward(20)
        self.turtles[0].left(90)
