from shutil import move
from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.create_ball()
    
    def create_ball(self):
        self.penup()
        self.shape('circle')
        self.color('White')
        # self.seth(randint(0, 360))
    
    def move_ball(self):
        # self.fd(20)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto((new_x, new_y))
        
    def collision_with_wall(self):
        if -280 > self.ycor() or self.ycor() > 280:
            self.y_move = -10