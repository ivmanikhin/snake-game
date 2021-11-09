from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, screen):
        super().__init__()
        scoreboard_pos = (0, (0.5 * screen.window_height() - 20))
        self.score = -1
        self.hideturtle()
        self.goto(scoreboard_pos)
        self.color("white")
        self.increase()

    def increase(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, align="center", font=("Courier", 14, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("YOU SUCK!", False, align="center", font=("Courier", 24, "bold"))
