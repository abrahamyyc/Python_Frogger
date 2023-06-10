from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.starting_x = 300
        self.end_x = -280
        self.x_move = 20
        self.hideturtle()
        self.color(self.choose_color())
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=2,stretch_wid=1)
        self.setheading(180)
        self.goto(self.starting_x, random.randint(-260, 260))
        self.showturtle()

    def choose_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        if r >= 230 or g >= 230:
            b = random.randint(0, 200)
        else:
            b = random.randint(0, 255)
        return r, g, b

    def move_car(self):
        new_x = self.xcor() - self.x_move
        self.goto(new_x, self.ycor())

    def increase_speed(self):
        self.x_move += 10