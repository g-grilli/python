
from turtle import *
from random import randint
bgcolor('yellow')
for i in range(4):
    penup()
    setpos(randint(-100, 100),randint(-100, 100,))
    pendown()
    for i in range(50):
        speed(9)
        pencolor('red')
        forward(50)
        left(125)

    for i in range(75):
        speed(9)
        pencolor('white')
        forward(75)
        right(125)

    for i in range(75):
        speed(9)
        pencolor('orange')
        forward(100)
        left(125)

    for i in range(75):
        speed(9)
        pencolor('red')
        forward(200)
        right(125)
mainloop()
