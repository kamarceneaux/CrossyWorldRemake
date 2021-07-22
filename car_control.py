COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random
import turtle

class CarManager():
    """Mocks a car function"""
    
    def __init__(self):
        """Initializes this function
        """
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_a_car(self):
        """Creates a car that will move accross the screen.
        """
        chance_for_car = random.randint(0,5)
        if chance_for_car == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
        
    def move_cars(self):
        """Moves the cars
        """
        for car in self.all_cars:
            car.backward(self.car_speed)
        
    def increase_speed(self):
        """Increases the speed of the cars by a number
        """
        self.car_speed += MOVE_INCREMENT
        