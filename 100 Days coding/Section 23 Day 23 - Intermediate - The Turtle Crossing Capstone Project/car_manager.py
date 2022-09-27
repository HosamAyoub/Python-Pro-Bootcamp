from random import randint
from secrets import choice
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.turtles = []
        
    def create(self):
        for _ in range(100):
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.shape('square')
            new_turtle.color(choice(COLORS))
            new_turtle.shapesize(stretch_len=2, stretch_wid=1)
            new_turtle.goto(randint(200, 2000), randint(-250, 280))
            self.turtles.append(new_turtle)
    
    def move(self, level):
        for t in self.turtles:
            t.goto(t.xcor() - STARTING_MOVE_DISTANCE - ((level - 1) * MOVE_INCREMENT), t.ycor())
            if t.xcor() < -350:
                t.goto(randint(350, 2000), t.ycor())
