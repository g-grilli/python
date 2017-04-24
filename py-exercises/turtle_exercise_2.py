#!usr/bin/env python 3
from turtle import *

#circle
side_length = 200
angle = 360 / 3

for i in range(3):
    forward(side_length)
    left(angle)


#square
side_length = 200
angle = 360 / 4

for i in range(4):
    forward(side_length)
    left(angle)


#pentagon
side_length = 200
angle = 360 / 5

for i in range(5):
    forward(side_length)
    left(angle)


#hexagon
side_length = 200
angle = 360 / 6

for i in range(6):
    forward(side_length)
    left(angle)


#octagon
side_length = 200
angle = 360 / 8

for i in range(8):
    forward(side_length)
    left(angle)


#star
for i in range(5):
    forward(300)
    left(144)


#circle
pencolor('green')
width(2)
circle(180)

mainloop()
