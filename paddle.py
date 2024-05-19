from turtle import Turtle, Screen

screen = Screen()


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=8)
        self.goto(position)

    def go_right(self):
        new_x = self.xcor() + 50
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 50
        self.goto(new_x, self.ycor())
