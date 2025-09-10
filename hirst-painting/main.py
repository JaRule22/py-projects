import colorgram
import turtle as t
import random as r

# rgb_colors = []
# colors = colorgram.extract("image.jpg", 25)
#
# color_tuple = ()
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

t.colormode(255)
color_list = [(199, 175, 118), (125, 36, 24), (187, 158, 50), (170, 105, 56), (5, 57, 83), (222, 223, 226), (200, 216, 205), (108, 67, 85), (39, 36, 35), (86, 142, 58), (20, 123, 176), (110, 161, 175), (75, 39, 47), (9, 67, 47), (64, 153, 137), (133, 41, 43), (184, 98, 80), (179, 201, 186), (210, 200, 113), (179, 175, 177), (151, 176, 164), (93, 142, 156), (28, 80, 59)]
starting_pos = [-500, -300]
x = starting_pos[0]
y = starting_pos[1]
t.teleport(starting_pos[0], starting_pos[1])

t.penup()
t.hideturtle()
t.speed("fastest")

for _ in range(10):
    y += 50
    t.teleport(x, y)
    for _ in range(10):
        random_color = color_list[r.randint(0, 22)]
        t.forward(25); t.dot(20, random_color); t.forward(25)

screen = t.Screen()
screen.exitonclick()