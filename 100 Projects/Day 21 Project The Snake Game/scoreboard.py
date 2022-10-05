from turtle import Turtle
FONT = ('Arial', 12, 'normal')
ALIGN = 'center'

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("data.txt", "r") as file:
                self.high_score = int(file.read())
        except:
            with open("data.txt", "w") as file:
                self.high_score = 0
                file.write(str(self.high_score))
        self.create_score_board()
    
    def create_score_board(self):
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.color('white')
        self.update_score_board()
        
    
    def update_score_board(self):
        self.clear()
        self.write(f"score: {self.score}  |  High score: {self.high_score}", move=False, align=ALIGN, font=(FONT))
        
    def increment_score(self):
        self.score += 1
        self.create_score_board()
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score_board()
        