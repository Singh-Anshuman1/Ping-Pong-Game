from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("PING PONG GAME")
screen.tracer(0)
paddle_r = Paddle(350)
paddle_l = Paddle(-350)
ball = Ball()

screen.listen()
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_l.go_down, "s")
screen.onkey(paddle_l.go_up, "w")

game = True
while game:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # detect collision with upper or lower wall
    if ball.ycor() > 280 or ball.ycor() < -280:  # bounce the ball back
        ball.bounce_y()
    # detect collision with right paddle and left paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # if right paddle misses
    if ball.xcor() > 380:
        ball.reset_positon()
    # if left paddle misses
    if ball.xcor() < -380:
        ball.reset_positon()


screen.exitonclick()
