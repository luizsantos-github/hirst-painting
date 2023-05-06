import turtle as t
import random


def set_random_color():
    color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213),
                  (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85),
                  (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48),
                  (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151)]

    return random.choice(color_list)


def draw_circles():
    for _ in range(10):
        bobo.dot(20, set_random_color())
        bobo.penup()
        bobo.forward(50)


def move_row(start_coordinates):
    new_coordinates = (start_coordinates[0], start_coordinates[1] + 50)
    return new_coordinates


start_x = -400
start_y = -300
t.colormode(255)

screen = t.Screen()
bobo = t.Turtle()
bobo.speed("fastest")

# Go to starting position
bobo.penup()
bobo.hideturtle()
bobo.setpos((start_x, start_y))
bobo.pendown()

# Draw Rows
for _ in range(10):
    current_coordinates = (bobo.xcor(), bobo.ycor())
    draw_circles()
    bobo.penup()
    bobo.setpos(move_row(current_coordinates))

screen.exitonclick()
