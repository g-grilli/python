#!usr/bin/env python 3
from turtle import *
import random

bgcolor('black')
setpos(-260, 155)
color('white')
begin_fill()
circle(90)
end_fill()
penup()

for i in range(200):
    setpos(random.randint(-210, 250),random.randint(-250, 250,))
    speed(9)
    color(random.choice(['blue','red', 'white' ]))
    for i in range (5):
        pendown()
        forward(10)
        left(144)
        penup()
mainloop()

if __name__ == "__main__":
    turtle_shapes(x)
