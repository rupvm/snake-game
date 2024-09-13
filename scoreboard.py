from turtle import Turtle

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("score.txt") as file:
            self.highscore=int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"score:{self.score} High Score:{self.highscore}", align='center', font=("Courier", 20, "normal"))

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("score.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score=0
        self.update_scoreboard()


    #def game_over(self):
        #self.goto(0, 0)
        #self.write(arg="Game over",align='center',font=("Courier",17,"normal"))


    def update(self):
        self.score+=1
        self.update_scoreboard()




