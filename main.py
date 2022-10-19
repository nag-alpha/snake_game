from turtle import Turtle, Screen
import time
import random

turts = []
initial_pos = [(0, 0), (-20, 0), (-40, 0)]


def create_snake():
    for i in range(3):
        turts.append(Turtle())
        turts[i].color("white")
        turts[i].shape("square")
        turts[i].penup()
        turts[i].goto(initial_pos[i])


def add_snake():
    turts.append(Turtle())
    turts[-1].penup()
    turts[-1].color("white")
    turts[-1].shape("square")
    turts[-1].goto(turts[-2].xcor(), turts[-2].ycor())


def move():
    for i in range(len(turts) - 1, 0, -1):
        x_cord = turts[i - 1].xcor()
        y_cord = turts[i - 1].ycor()
        turts[i].goto(x_cord, y_cord)
    turts[0].forward(20)


def up():
    for i in range(len(turts) - 1, 0, -1):
        x_cord = turts[i - 1].xcor()
        y_cord = turts[i - 1].ycor()
        turts[i].goto(x_cord, y_cord)
    if turts[0].heading() != DOWN:
        turts[0].setheading(UP)
    turts[0].forward(20)


def down():
    for i in range(len(turts) - 1, 0, -1):
        x_cord = turts[i - 1].xcor()
        y_cord = turts[i - 1].ycor()
        turts[i].goto(x_cord, y_cord)
    if turts[0].heading() != UP:
        turts[0].setheading(DOWN)
    turts[0].forward(20)


def left():
    for i in range(len(turts) - 1, 0, -1):
        x_cord = turts[i - 1].xcor()
        y_cord = turts[i - 1].ycor()
        turts[i].goto(x_cord, y_cord)
    if turts[0].heading() != RIGHT:
        turts[0].setheading(LEFT)
    turts[0].forward(20)


def right():
    for i in range(len(turts) - 1, 0, -1):
        x_cord = turts[i - 1].xcor()
        y_cord = turts[i - 1].ycor()
        turts[i].goto(x_cord, y_cord)
    if turts[0].heading() != LEFT:
        turts[0].setheading(RIGHT)
    turts[0].forward(20)


screen = Screen()
screen.title("Snake game")
screen.bgcolor("black")
screen.setup(600, 600)
screen.tracer(0)

create_snake()

screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

score = Turtle()
s = 1
score.color("white")
score.penup()
score.goto(0, 260)
score.hideturtle()

wall = Turtle()
wall.color("white")
wall.hideturtle()

food = Turtle()
food.shapesize(0.7, 0.7)
food.color("blue")
food.penup()
food.shape("circle")
food.speed("fastest")
xcordinate = random.randint(-280, 280)
ycordinate = random.randint(-280, 280)
food.goto(xcordinate, ycordinate)


def refresh():
    xcord = random.randint(-280, 280)
    ycord = random.randint(-280, 260)
    food.goto(xcord, ycord)


UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0
screen = Screen()



score.write(arg="Score = 0", align="center", font=("Arial", 24, "normal"))

game_on = True
while game_on:
    screen.update()
    time.sleep(0.08)

    move()

    if turts[0].distance(food) <= 25:
        score.clear()
        score.write(arg=f"Score = {s}", align="center", font=("Arial", 24, "normal"))
        refresh()
        add_snake()
        s = s + 1
    if turts[0].xcor() < -300 or turts[0].xcor() > 300 or turts[0].ycor() < -300 or turts[0].ycor() > 300:
        game_on = False
        wall.write(arg="Game over", align="center", font=("Arial", 24, "normal"))
    for turtles in turts:
        if turtles == turts[0]:
            pass
        elif turts[0].distance(turtles) < 10:
            game_on = False
            wall.write(arg="Game over", align="center", font=("Arial", 24, "normal"))

screen.exitonclick()
