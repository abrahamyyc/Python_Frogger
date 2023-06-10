from turtle import Turtle


class TurtleFrog(Turtle):
    def __init__(self):
        super().__init__()
        self.starting_position = (0, -280)
        self.hideturtle()
        self.color("aquamarine")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(self.starting_position)
        self.showturtle()

    def go_up(self):
        self.setheading(90)
        self.forward(20)

    def go_left(self):
        self.setheading(180)
        self.forward(20)

    def go_right(self):
        self.setheading(0)
        self.forward(20)

    def reset_position(self):
        self.hideturtle()
        self.goto(self.starting_position)
        self.showturtle()