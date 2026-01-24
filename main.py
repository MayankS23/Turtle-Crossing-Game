from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
l_scoreboard = Scoreboard(-100)
r_scoreboard = Scoreboard(100)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
r_player_score = 0
l_player_score = 0
speed_time = 0.1

while game_is_on:

    time.sleep(speed_time)
    screen.update()
    ball.move()

    #detect collision with wall

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 320 and ball.distance(r_paddle) < 50:
        ball.bounce_x()
        speed_time -= 0.02
        time.sleep(speed_time)


    elif ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
        speed_time -= 0.02
        time.sleep(speed_time)

    if ball.xcor() > 380:
        speed_time = 0.1
        l_player_score += 1
        l_scoreboard.increase_score(l_player_score)
        ball.reset_position()
        ball.bounce_x()

    elif ball.xcor() < -380:
        speed_time = 0.1
        r_player_score += 1
        r_scoreboard.increase_score(r_player_score)
        ball.reset_position()
        ball.bounce_x()


screen.exitonclick()
