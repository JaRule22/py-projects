from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import turtle as t

def display():
    """This function will display the game"""
    t.hideturtle()
    t.teleport(x=0, y=300)
    t.right(90)
    t.pensize(3)

    for line in range(34):
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)

screen = Screen()
screen.tracer(0)
r_paddle = Paddle(350,0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")

t.color("white")
t.speed("fastest")

t.penup()
display()

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with r_paddle and l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect R paddle misses and L paddle misses
    if ball.xcor() > 420:
        ball.x_move = -10
        ball.reset_ball()
        scoreboard.l_point()
    elif ball.xcor() < -420:
        ball.x_move = 10
        ball.reset_ball()
        scoreboard.r_point()





screen.exitonclick()