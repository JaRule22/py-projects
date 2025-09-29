import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
sleep_number = 0.1
while game_is_on:
    time.sleep(sleep_number)
    screen.update()
    screen.bgcolor("gray")

    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    # #Detect finish line
    if player.finish_line():
        car_manager.level_up()
        scoreboard.increase_level()
        scoreboard.update_scoreboard()

screen.exitonclick()