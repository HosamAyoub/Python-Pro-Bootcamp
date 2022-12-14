from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    
    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)
            
    
    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.shapesize()
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    
    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for turtle in range(len(self.segments) - 1, 0, -1):
            new_pos = (self.segments[turtle - 1].position())
            self.segments[turtle].goto(new_pos)
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