from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
    
    def create_ball(self):
        self.penup()
        self.shape('circle')
        self.color('White')
        self.seth(randint(0, 360))
    
    def move_ball(self):
        self.fd(20)