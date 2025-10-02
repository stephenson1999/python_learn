# #1
import turtle
sc = turtle.Screen()
sc.bgcolor("green")
sc.setup(1000,1000)
sc.title("Welcome to Python Turtle")
board = turtle.Turtle()

turtle.penup()
turtle.goto(250,-250)
for n in range(3):
    turtle.pendown()
    turtle.forward(100)
    turtle.left(120)
turtle.penup()

turtle.goto(350, 150)
for n in range(2):
    turtle.pendown()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
turtle.penup()

turtle.goto(-200, -200)
for n in range(6):
    turtle.pendown()
    turtle.left(60)
    turtle.forward(50)


turtle.exitonclick()



