from shutil import move
from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
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
        self.x_move *= -1
    
    def reset(self):
        self.goto((0, 0))
        self.x_bounce()