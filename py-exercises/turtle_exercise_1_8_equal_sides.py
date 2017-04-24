#!usr/bin/env python 3
from turtle import *

side_length = int(input("what line length? "))
num_sides = int(input("How many sides? "))
for i in range(num_sides):
    angle = 360 / num_sides
    forward(side_length)
    left(angle)
mainloop()
