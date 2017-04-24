#!usr/bin/env python 3

from turtle import *

def equ_triangle():
    for i in range(3):
        side_length = 200
        angle = 360 / 3
        forward(side_length)
        left(angle)

def square():
    for i in range(4):
        side_length = 200
        angle = 360 / 4
        forward(side_length)
        left(angle)

def pentagon():
    for i in range(5):
        side_length = 50
        angle = 360 / 5
        forward(side_length)
        left(angle)

def hexagon():
    for i in range(6):
        side_length = 50
        angle = 360 / 6
        forward(side_length)
        left(angle)

def octagon():
    for i in range(8):
        side_length = 50
        angle = 360 / 8
        forward(side_length)
        left(angle)

def star():
    for i in range(5):
        forward(300)
        left(144)

def circle():
    pencolor('green')
    width(2)
    circle(90)


if __name__ == "__main__":
    turtle_shapes(x)
