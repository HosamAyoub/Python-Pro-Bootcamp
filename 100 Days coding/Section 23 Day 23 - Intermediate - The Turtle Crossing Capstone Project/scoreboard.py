from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-290, 260)
        self.level = 1
        self.update_level()
        
    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align='left', font=FONT)
    
    def next_level(self):
        self.level += 1
        self.update_level()
