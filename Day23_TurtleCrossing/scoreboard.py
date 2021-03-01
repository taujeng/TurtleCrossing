FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, multiplier):
        super().__init__()
        self.penup()
        self.goto(-215, 260)
        self.hideturtle()
        self.write(f"LEVEL: 1", align="left",font=FONT)

    def lvl(self, multiplier):
        self.clear()
        self.write(f"LEVEL: {multiplier+1}", align="left", font=FONT)

    def over(self):
        self.goto(0, 0)
        self.write("GME OVER", align="center", font=("Comic", 25,"bold"))