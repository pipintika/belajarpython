from turtle import *

pensize(2)
bgcolor('wheat')

penup()
goto(-135, 100)
setheading(-90)
pendown()
color('floral white')
begin_fill()
for i in range(2):
    forward(200)
    circle(10, 90)
    forward(250)
    circle(10, 90)
end_fill()

color('brown')
begin_fill()
penup()
goto(-140, 100)
setheading(-90)
pendown()
forward(100)
circle(20, 180)
forward(50)
circle(-20, 180)
forward(30)
circle(20, 180)
forward(50)
circle(-20, 180)
forward(40)
circle(20, 180)
forward(30)
circle(-20, 180)
forward(60)
circle(20, 180)
forward(100)
circle(140, 180)
end_fill()

penup()
goto(-30, -110)
pendown()
color('burlywood')
begin_fill()
forward(100)
circle(30, 180)
forward(100)
left(90)
forward(60)
end_fill()

hideturtle()
done()

