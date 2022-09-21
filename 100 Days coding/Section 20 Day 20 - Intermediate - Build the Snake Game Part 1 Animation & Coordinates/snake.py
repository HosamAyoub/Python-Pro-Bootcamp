from turtle import Turtle

class Snake:
    def __init__(self):
        self.turtles = []
        self.x_positions = [0, -20, -40]
        for x_pos in self.x_positions:
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
