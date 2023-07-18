from turtle import*
speed('slowest')
bgcolor('black')

def polygon(sides,length,color,width):
    pencolor(color)
    pensize(width)
    for i in range(sides):
        forward(length)
        right(360/sides)

polygon(4,100,'red',4) #square
polygon(6,50,'green',2) #hexagon
polygon(3,100,'blue',3) #triangle


hideturtle()
mainloop()