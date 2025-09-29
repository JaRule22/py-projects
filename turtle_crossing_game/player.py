from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(to_angle=90)
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.ycor()

    def up(self):
        """This function moves the player up when the up key is pressed"""
        return self.forward(MOVE_DISTANCE)

    #Need to create a function that dictates if the player touched the finish line
    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        else:
            return False