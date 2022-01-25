from turtle import Turtle
with open("data.txt",) as game_data:
    current_highest_score = int(game_data.read())


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.high_score = current_highest_score
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score:{self.score}  High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score}  High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()


    #
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align="center", font=("Courier", 24, "normal"))


