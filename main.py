from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time


speed = 1
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")
max_screen_x = 0.5 * screen.window_width() - 10
max_screen_y = 0.5 * screen.window_height() - 10

scoreboard = Scoreboard(screen)
snake = Snake()
food = Food(screen)
screen.update()

game_is_on = True

screen.listen()
screen.onkeypress(fun=snake.turn_right, key="Right")
screen.onkeypress(fun=snake.turn_left, key="Left")
screen.onkeypress(fun=snake.turn_up, key="Up")
screen.onkeypress(fun=snake.turn_down, key="Down")

while game_is_on:
    snake.step()
    screen.update()
    time.sleep(1 / (4 + speed))
    if abs(snake.snake[0].xcor()) >= max_screen_x or abs(snake.snake[0].ycor()) >= max_screen_y or snake.bite_tail():
        scoreboard.reset()
        snake.reset()
        speed = 1
    if snake.head.distance(food.pos()) < 10:
        food.new_pos(screen)
        snake.grow()
        scoreboard.increase()
        if scoreboard.score % 10 == 0:
            speed += 1

screen.exitonclick()
