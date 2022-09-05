import turtle

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.pencolor("green")
t.speed(100)
c=0
d=0
while True:
    for i in range(4):
        t.forward(80)
        t.right(90)
    t.right(5)
    c+=1
    if c>=390/5:
         break
t.hideturtle()

turtle.done()