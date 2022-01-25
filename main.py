from turtle import Screen
import time
from snake import Snake
from Food import Food
from scoreboard import ScoreBoard

game_screen = Screen()
game_screen.setup(width=600, height=600)
game_screen.bgcolor("black")
game_screen.title("Snake Game")
game_screen.tracer(0)
score = 0
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

game_screen.listen()
game_screen.onkey(snake.up, "Up")
game_screen.onkey(snake.down, "Down")
game_screen.onkey(snake.left, "Left")
game_screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    game_screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect if there is any collision with the tail

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()

game_screen.exitonclick()
