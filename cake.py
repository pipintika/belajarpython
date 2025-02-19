from turtle import*

speed(5)
pensize(5)
bgcolor('black')

def draw_layer(width, x,y):
    color('deep pink','hot pink')
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    forward(width)
    circle(10, 90)
    forward(80)
    circle(10, 90)
    forward(width)
    circle(10, 90)
    forward(80)
    circle(10, 90)
    end_fill()

def draw_coklat(width, x, y, repeat):
    color('saddle brown','sienna')
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    forward(width)
    circle(-10, 90)
    forward(30)
    for i in range(repeat):
        circle(-15, 180)
        circle(15, 180)
    circle(-15, 180)
    forward(30)
    circle(-10, 90)
    end_fill()
def draw_line(x, y, width):
    color('purple')
    penup()
    goto(x, y)
    pendown()
    forward(width)

def draw_candle():
    color('white')
    penup()
    goto(-5, 100)
    pendown()
    begin_fill()
    for i in range(2):
        forward(10)
        left(90)
        forward(80)
        left(90)
    end_fill()
    penup()
    goto(0, 180)
    left(90)
    pendown()
    forward(10)
    penup()
    pensize(1)
    forward(40)
    left(160)
    pendown()
    color('orange')
    begin_fill()
    forward(30)
    setheading(-90)
    circle(10, 180)
    left(20)
    forward(30)
    end_fill()

draw_layer(370, -180, -200)
draw_layer(310, -150, -100)
draw_layer(250, -120, 0)

draw_coklat(370, -180, -100, 6)
draw_coklat(310, -150, 0, 5)
draw_coklat(250, -120, 100, 4)

draw_line(-190, -170, 390)
draw_line(-190, -180, 390)
draw_line(-160, -80, 330)
draw_line(-160, -70, 330)
draw_line(-130, 20, 270)
draw_line(-130, 30, 270)

draw_candle()

hideturtle()
done()
