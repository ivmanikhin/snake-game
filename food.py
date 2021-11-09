from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.new_pos(screen)

    def new_pos(self, screen):
        max_screen_x = 0.5 * screen.window_width() - 20
        max_screen_y = 0.5 * screen.window_height() - 20
        random_coord = (randint(-int(max_screen_x / 20), int(max_screen_x / 20)) * 20,
                        randint(-int(max_screen_y / 20), int(max_screen_y / 20)) * 20)
        self.goto(random_coord)
