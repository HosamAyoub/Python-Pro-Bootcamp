from random import randint
from secrets import choice
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 4
MOVE_INCREMENT = 2


class CarManager():
    def __init__(self):
        self.turtles = []
        self.speed = STARTING_MOVE_DISTANCE
        
    def create(self):
        for _ in range(100):
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.shape('square')
            new_turtle.color(choice(COLORS))
            new_turtle.shapesize(stretch_len=2, stretch_wid=1)
            new_turtle.goto(randint(-200, 2000), randint(-250, 280))
            self.turtles.append(new_turtle)
    
    def move(self):
        for t in self.turtles:
            t.backward(self.speed)
            if t.xcor() < -350:
                t.goto(randint(250, 2000), randint(-250, 280))
            
    def speed_up(self):
        self.speed += MOVE_INCREMENT
