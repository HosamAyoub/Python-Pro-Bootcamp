import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.title('Crossing Capstone')
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
car_manager.create()

screen.listen()
screen.onkeypress(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    for car in car_manager.turtles:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.finish():
        scoreboard.level_up()
        car_manager.speed_up()
    car_manager.move()
    screen.update()

screen.exitonclick()