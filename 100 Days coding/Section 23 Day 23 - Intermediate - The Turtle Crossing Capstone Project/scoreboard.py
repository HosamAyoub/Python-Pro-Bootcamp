from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(-290, 260)
        self.level = 1
        self.update_level()
        
    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align='left', font=FONT)
    
    def level_up(self):
        self.level += 1
        self.update_level()
    
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align='center', font= ("Courier", 18, "bold"))
