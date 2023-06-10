from turtle import Screen, Turtle
from frog import TurtleFrog
from cars import Car
from scoreboard import Scoreboard
import time
import random

window = Screen()
window.setup(600, 600)
window.bgcolor("blue")
window.colormode(255)
window.tracer(0)

road = Turtle()
road.color("gray")
road.shape("square")
road.shapesize(stretch_len=30, stretch_wid=11)

froggy = TurtleFrog()

window.listen()
window.onkey(froggy.go_up, "w")
window.onkey(froggy.go_left, "a")
window.onkey(froggy.go_right, "d")

scoreboard = Scoreboard()

play_game = True
cars_list = []
upper_limit = 6

while play_game:
    time.sleep(0.1)
    window.update()
    if random.randint(1, upper_limit) == 1:
        new_car = Car()
        cars_list.append(new_car)
    for car in cars_list:
        car.move_car()
        # detect collision with car
        if car.distance(froggy) < 20:
            scoreboard.game_over()
            play_game = False
    # detect reaching end of the top of window
    if froggy.ycor() >= 300:
        scoreboard.increase_level()
        for car in cars_list:
            car.increase_speed()
        if upper_limit > 2:
            upper_limit -= 1
        froggy.reset_position()


window.exitonclick()