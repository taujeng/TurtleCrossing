COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle, Screen
import random


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.allcars = []

    def create_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.turtlesize(stretch_wid=1, stretch_len=2, outline=1)
            pos = random.randint(-240, 240)
            new_car.goto(280, pos)
            self.allcars.append(new_car)

    def move(self, multiplier):
        for car in self.allcars:
            car.backward(STARTING_MOVE_DISTANCE+(5*multiplier))



