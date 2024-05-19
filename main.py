from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from wall import Wall
from scoreboard import Scoreboard


# Function to write a title on the screen
def write_title():
    title_turtle = Turtle()
    title_turtle.hideturtle()
    title_turtle.penup()
    title_turtle.color("white")
    title_turtle.goto(0, 350)  # Position the title at the top of the screen
    title_turtle.write("Pong Game", align="center", font=("Courier", 24, "normal"))


# Creating the screen
screen = Screen()
screen.tracer(0)
screen.setup(900, 800)
screen.bgcolor("black")
screen.title("Pong")


# Write the title on the screen
write_title()

paddle = Paddle((0, -350))
ball = Ball()
scoreboard = Scoreboard()

# Set up key bindings
screen.listen()
screen.onkey(key="Left", fun=paddle.go_left)
screen.onkey(key="Right", fun=paddle.go_right)

wall = Wall(rows=12, columns=25)
wall.create_bricks()
wall.display_wall()

# Main Game Loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect the collision with the top wall
    if ball.ycor() > 300:
        ball.bounce_y()

    # Detect the collision with the side walls
    if ball.xcor() > 400 or ball.xcor() < -400:
        ball.bounce_x()

    # Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -340:
        ball.bounce_y()

    # Detect when paddle misses
    if ball.ycor() < -350:
        ball.reset_position()
        scoreboard.decrease_point()


    # Detect collision with wall
    if wall.check_collision(ball):
        scoreboard.increase_point()

screen.exitonclick()
