import turtle



wn = turtle.Screen()
wn.title("test")
wn.bgcolor("white")


b = turtle.Turtle()
b.speed(10)
b.begin_fill()
for i in range (100):
    b.forward(i**(2))
    b.left(i%90)
    b.forward(i**(2))
b.end_fill()

















turtle.done()

