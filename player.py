STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    """Mocks a Turtle object

    """
    def __init__(self) -> None:
        super().__init__()
        self.create_turtle()
        self.score = 0
        
    def create_turtle(self):
        """Creates a turtle object.
        """
        self.color('black')
        self.shape('turtle')
        self.penup()
        self.goto(x=0, y=-275)
        self.setheading(90)

    def move_turtle(self):
        """Moves the turtle forward by move distance (default=10)
        """
        self.forward(MOVE_DISTANCE)
    
    def detect_end(self):
        """Detect when a player reached the top of the screen without dying. Returns True when that happened
        """
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(0, -275)
            return True
        else:
            return False