from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("blue")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-270, 260)
        random_y = random.randint(-270, 260)
        self.goto(random_x, random_y)