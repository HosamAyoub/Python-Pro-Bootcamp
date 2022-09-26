from turtle import Turtle

NORTH = 90
STEP = 10

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)
    
    def create_paddle(self, position):
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color('White')
        self.seth(NORTH)
        self.goto(position)
    
    def up(self):
        self.fd(STEP)
        
    def down(self):
        self.bk(STEP)