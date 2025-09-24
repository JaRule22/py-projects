from turtle import Turtle

class Paddle(Turtle):
    """This class is the default paddle for the game"""
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.penup()
        self.goto(x=x_pos, y=y_pos)
        self.shape(name="square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        """This will move the paddle up when the up button is pressed"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        """This will move the paddle up when the down button is pressed"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)