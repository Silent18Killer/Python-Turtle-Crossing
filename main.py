from turtle import Turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

turtle = Turtle()
turtle.hideturtle()

my_screen = Screen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard() 

my_screen = Screen()
my_screen.setup(600, 600)
my_screen.title("Turtle Crossing - Capstone Project")
my_screen.tracer(0)

my_screen.listen()
my_screen.onkey(player.go_up, "W")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    my_screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

my_screen.exitonclick()