from turtle import Turtle

SOUTH = 270

FONT = ('Courier', 60, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        self.middle_line()
    
    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=FONT)
        self.middle_line()
    
    def l_point(self):
        self.l_score += 1
        self.update_score()
        
    def r_point(self):
        self.r_score += 1
        self.update_score()
    
    def middle_line(self):
        self.speed('fastest')
        self.pen(fillcolor= 'white', pencolor= 'white')
        self.pensize(5)
        self.penup()
        self.goto(0, 300)
        self.seth(SOUTH)
        while self.ycor() > -300:
            self.pendown()
            self.forward(30)
            self.penup()
            self.forward(30)