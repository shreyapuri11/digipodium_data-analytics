from turtle import *
pencolor('red')
pensize(2)
bgcolor('black')
 
def square():
    for i in range(4):
        forward(100)
        right(90)
def pentagon():
    for i in range(5):
        forward(100)
        right(72)

#for i in range(5)
# fd(200)
#pentagon()
#right(72)

square()
pentagon()
goto(200, 0)
square()
pentagon()

hideturtle()
mainloop()