from turtle import Turtle

BRICK_WIDTH = 30
BRICK_HEIGHT = 30
BRICK_GAP = 3  # Gap between bricks

class Wall:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.bricks = []  # List to store brick information (position, color, status)

    def create_bricks(self):
        # Calculate starting position for the top-left brick
        start_x = -((self.columns * (BRICK_WIDTH + BRICK_GAP)) / 2) + BRICK_WIDTH / 2
        start_y = 250  # Adjust as needed

        for row in range(self.rows):
            for col in range(self.columns):
                brick = Turtle()
                brick.shape("square")
                brick.color("red")  # Customize brick color based on row
                brick.shapesize(stretch_wid=BRICK_HEIGHT/20, stretch_len=BRICK_WIDTH/20)
                brick.penup()
                brick.goto(start_x + col * (BRICK_WIDTH + BRICK_GAP), start_y - row * (BRICK_HEIGHT + BRICK_GAP))
                self.bricks.append(brick)

    def check_collision(self, ball):
        for brick in self.bricks:
            if brick.isvisible() and ball.distance(brick) < 25:
                print("Collision detected with brick!")
                brick.hideturtle()  # Hide the brick from the screen
                self.bricks.remove(brick)  # Remove brick from the list
                ball.bounce_y()  # Make the ball bounce off
                return True  # Collision detected

        return False  # No collision

    def display_wall(self):
        for brick in self.bricks:
            brick.showturtle()  # Ensure the brick is visible
