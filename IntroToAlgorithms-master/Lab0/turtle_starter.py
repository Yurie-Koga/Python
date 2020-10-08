import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")


def draw_square(length: int):
    for _ in range(4):
        t.forward(length)
        t.right(90)


draw_square(200)
draw_square(100)

screen.exitonclick()
