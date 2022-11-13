from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

snake = []

for i in range(0, 3):
    new_snake = Turtle("square")
    new_snake.color("white")
    new_snake.goto(x=0 - (20 * i), y=0)
    snake.append(new_snake)

screen.exitonclick()
