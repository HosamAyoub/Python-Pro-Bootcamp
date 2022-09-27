from shutil import move
from turtle import Turtle, xcor
from random import randint

DELAY = 0.09

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = DELAY
        self.create()
    
    def create(self):
        self.penup()
        self.shape('circle')
        self.color('White')
    
    def move(self):
        
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto((new_x, new_y))
        
    def y_bounce(self):
        self.y_move *= -1
    
    def x_bounce(self):
        if self.xcor() > 0:
            self.x_move = -(abs(self.x_move))
        else:
            self.x_move = abs(self.x_move)
        self.move_speed *= 0.9
    
    def reset(self):
        self.move_speed = DELAY
        self.goto((0, 0))
        self.x_bounce()