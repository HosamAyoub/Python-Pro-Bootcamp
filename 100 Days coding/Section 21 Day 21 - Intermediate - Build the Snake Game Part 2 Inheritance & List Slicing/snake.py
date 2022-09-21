from turtle import Turtle

X_STARTING_POSITIONS = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]
    
    
    def create_snake(self):
        for x_pos in X_STARTING_POSITIONS:
            new_turtle = Turtle(shape='square')
            new_turtle.shapesize()
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
        if self.head.heading() != DOWN:
            self.head.seth(UP)
    
    
    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
    
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
        
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)