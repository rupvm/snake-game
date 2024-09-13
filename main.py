from turtle import Turtle,Screen
import time
from Snake import Snake
from food import Food
from scoreboard import scoreboard

screen=Screen()
screen.tracer(0)
screen.setup(width=600,height=600)
screen.title("My snake game")
screen.bgcolor("black")

snake=Snake()
food=Food()
score=scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        print("nom nom nom")
        food.refresh()
        score.update()
        snake.extend()

    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        score.reset()
        snake.reset()

    for seg in snake.all_segments[1:]:
        if snake.head.distance(seg)<10:
            score.reset()
            snake.reset()



screen.exitonclick()