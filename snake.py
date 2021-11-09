from turtle import Turtle, Screen
import time
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    snake = []

    def __init__(self, length=3):
        self.snake.append(Turtle("square"))
        self.head = self.snake[0]
        for segment in range(length):
            self.grow()

    def turn_left(self):
        if self.head.heading() in [UP, DOWN]:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() in [UP, DOWN]:
            self.head.setheading(RIGHT)

    def turn_up(self):
        if self.head.heading() in [LEFT, RIGHT]:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() in [LEFT, RIGHT]:
            self.head.setheading(DOWN)

    def step(self, speed):

        for segment in reversed(self.snake[1:]):
            segment.goto(self.snake[self.snake.index(segment) - 1].pos())
        self.head.forward(20)

    def grow(self):
        self.snake.append(Turtle("square"))
        self.snake[-1].shapesize(0.9, 0.9)
        self.snake[-1].penup()
        self.snake[-1].color("white")
        self.snake[-1].goto(self.snake[-2].pos())

    def bite_tail(self):
        for segment in self.snake[1:]:
            if segment.distance(self.head.pos()) < 10:
                return True
        return False
