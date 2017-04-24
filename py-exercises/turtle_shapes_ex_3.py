#!usr/bin/env python 3
from turtle import *

def shape_maker(side_length, sides, p_color, f_color):
    begin_fill()
    pencolor(p_color)
    fillcolor(f_color)
    for i in range(sides):
        angle = 360 / sides
        forward(side_length)
        left(angle)
    end_fill()


def star(length, p_color, f_color):
    begin_fill()
    pencolor(p_color)
    fillcolor(f_color)
    for i in range(5):
        forward(length)
        left(144)
    end_fill

def draw_circle():
    begin_fill()
    pencolor('green')
    fillcolor('red')
    width(2)
    circle(90)
    end_fill


#if __name__ == "__main__":
#    turtle_shapes_ex_3(x)
