import turtle

wn=turtle.Screen()
wn.title("pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)


#score 

sa=0
sb=0


#padla a
pa=turtle.Turtle()
pa.speed(-2)
pa.shape("square")
pa.shapesize(stretch_wid=5,stretch_len=1)
pa.color("white")
pa.penup()
pa.goto(-350,0)


#padle b
pb=turtle.Turtle()
pb.speed(0)
pb.shape("square")
pb.shapesize(stretch_wid=5,stretch_len=1)
pb.color("white")
pb.penup()
pb.goto(350,0)

#ball
b = turtle.Turtle()
b.speed(0)
b.shape("square")
b.color("white")
b.penup()
b.goto(0, 0)
b.dx = 2
b.dy = 2


#♦pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


#function 
def paup():
    y=pa.ycor()
    y+=20
    pa.sety(y)
    
def pbup():
    y=pb.ycor()
    y+=20
    pb.sety(y)
    
def padown():
    y=pa.ycor()
    y-=20
    pa.sety(y)
    
def pbdown():
    y=pb.ycor()
    y-=20
    pb.sety(y)

#keybord binding

wn.listen()
wn.onkeypress(paup,"s")
wn.onkeypress(padown,"w")
wn.onkeypress(pbup,"Up")
wn.onkeypress(pbdown,"Down")




#main game loop

while True :
    wn.update()
    #move the ball
    b.setx(b.xcor()+b.dx)
    b.sety(b.ycor()+b.dy)
    #border checking
    if b.ycor()>290:
        b.sety(290)
        b.dy*=-1
    if b.ycor()<-290:
        b.sety(-290)
        b.dy*=-1
    if b.xcor()>390:
        b.goto(0,0)
        b.dx*=-1
        sa+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(sa,sb), align="center", font=("Courier", 24, "normal"))
    if b.xcor()<-390:
        b.goto(0,0)
        b.dx*=-1
        sb+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(sa,sb), align="center", font=("Courier", 24, "normal"))
    #padle and ball colision
    
    if (b.xcor()>340 and b.xcor()<350)  and (b.ycor()<pb.ycor()+40 and b.ycor()>pb.ycor()-40):
        b.setx(340)
        b.dx*=-1
        
    if (b.xcor()<-340 and b.xcor()>-350) and (b.ycor()<pa.ycor()+40 and b.ycor()>pa.ycor()-40):
        b.setx(-340)
        b.dx*=-1
        
        
    