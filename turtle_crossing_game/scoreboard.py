from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setpos(-280, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        """This function will update the scoreboard and change the level as soon as
           the player crosses the finish line."""
        self.write(f"Level {self.score}", font=FONT)

    def increase_level(self):
        """This function will increase the level everytime when the  player crosses the
           finish line."""
        self.clear()
        self.score += 1