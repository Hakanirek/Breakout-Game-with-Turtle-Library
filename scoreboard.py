from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 20, "normal"))


    def increase_point(self):
        self.score += 10
        self.update_scoreboard()

    def decrease_point(self):
        self.score -= 50
        self.update_scoreboard()
