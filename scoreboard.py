from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, screen):
        super().__init__()
        scoreboard_pos = (0, (0.5 * screen.window_height() - 20))
        self.score = -1
        with open('high_score.txt') as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.goto(scoreboard_pos)
        self.color("white")
        self.increase()

    def increase(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}   High score: {self.high_score}", False, align="center", font=("Courier", 14, "bold"))

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open('high_score.txt', mode='w') as file:
                file.write(str(self.high_score))
        self.score = -1
        self.increase()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("YOU SUCK!", False, align="center", font=("Courier", 24, "bold"))
