import turtle
screen=turtle.Screen()
screen.bgcolor("blue")
screen.title("Python Turtle")
turtle_instance=turtle.Turtle()
turtle_instance.left(36)
while True:
    turtle_instance.forward(random.randint(0,50))
    turtle_instance.right(random.randint(0,360))