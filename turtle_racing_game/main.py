from turtle import Turtle, Screen
import random

screen = Screen()
is_race_on = False

screen.setup(width=500 , height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
index = 0

x_axis = -230
y_axis = -100
all_turtles = []

#This loop sets the turtle color, its starting position, and add a new turtle obj to the all_turtle list
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=x_axis, y=y_axis)
    y_axis += 35
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

""" This while loop determines whether the race is still going on, if not, then it will end the race.
    It will also determine the winner."""
while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()