import time
from turtle import Screen
from car_control import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#Create a Player Object
user = Player()

#Create a car object
car_manager = CarManager()

#Initalize scoreboard
score_screen = Scoreboard()

#Listens for keystrokes
screen.listen()
screen.onkey(user.move_turtle, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_a_car()
    car_manager.move_cars()
    
    #Determine if a player hit a car
    for car in car_manager.all_cars:
        if user.distance(car) < 21 and (car.xcor() < 10 or car.xcor() > -10):
            game_is_on = False
    
    #Determine when the player reached the top of the screen and increase car speed
    if user.detect_end() == True:
        user.score += 1
        car_manager.increase_speed()
        score_screen.create_screen(user.score)
        
      
score_screen.end_screen()
screen.exitonclick()
