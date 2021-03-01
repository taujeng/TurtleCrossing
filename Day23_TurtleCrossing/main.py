import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
import random
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
multiplier = 0
score = Scoreboard(multiplier)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkey(player.up, "Up")
    screen.onkey(player.down, "Down")
    car_manager.create_car()
    car_manager.move(multiplier)
    for cars in car_manager.allcars:
        if cars.distance(player) < 20:
            game_is_on = False
            score.over()
    if player.ycor() > 280:
        player.goto(0, -280)
        multiplier += 1
        score.lvl(multiplier)







screen.exitonclick()