from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
NORTH = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.seth(NORTH)
        self.start()
    
    def start(self):
        self.goto(STARTING_POSITION)
    
    def up(self):
        self.goto(x=0, y=self.ycor() + MOVE_DISTANCE)
    
    def finish(self):
        if self.ycor() > FINISH_LINE_Y:
            self.start()
            return True
        return False