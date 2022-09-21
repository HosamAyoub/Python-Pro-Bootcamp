from turtle import Turtle
FONT = ('Arial', 12, 'normal')
ALIGN = 'center'

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.create_score_board()
    
    def create_score_board(self):
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.color('white')
        self.write(f"score: {self.score}", move=False, align=ALIGN, font=(FONT))
        
    def increment_score(self):
        self.score += 1
        self.clear()
        self.create_score_board()
        