FONT = ("Courier", 24, "normal")
from turtle import Turtle
from player import FINISH_LINE_Y



class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.create_screen()
        
        
    def create_screen(self, score=0):
        """Creates the scoreboard screen.
        """
        self.hideturtle()
        self.penup()
        self.color('black')
        self.clear()
        self.goto(x=-225, y=FINISH_LINE_Y-25)
        self.write(f"Level: {score}", align='center', font=FONT)
        
    def end_screen(self):
        """Shows the game over screen :(
        """
        self.hideturtle()
        self.pencolor()
        self.color('black')
        self.goto(0,0)
        self.write("GAME OVER", align='center', font=FONT)
