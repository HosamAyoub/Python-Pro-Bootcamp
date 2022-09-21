from turtle import Turtle

X_STARTING_POSITIONS = [0, -20, -40]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]
    
    
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
        self.head.forward(MOVE_DISTANCE)
    
    
    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)
    
    
    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)
    
    
    def right(self):
        if self.head.heading() != 180:
            self.head.seth(0)
        
    
    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)