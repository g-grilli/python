#!usr/bin/env python 3
from turtle import *

#side_length = int(input("what line length? "))
#num_sides = int(input("How many sides? "))
def pentagon():
    for i in range(5):
        side_length = 200
        angle = 360 / 5
        forward(side_length)
        left(angle)

mainloop()
