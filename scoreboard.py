from turtle import Turtle

ALIGN = "left"
FONT = "Times New Roman", 12, "bold"
GAME_OVER_ALIGN = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.hideturtle()
        self.penup()
        self.goto(-270, 270)
        self.color("black")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.current_level}", align=ALIGN, font=FONT)

    def increase_level(self):
        self.clear()
        self.current_level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over! You got squished!", align="center", font=FONT)