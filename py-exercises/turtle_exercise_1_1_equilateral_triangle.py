#!usr/bin/env python 3
from turtle import *
side_length = 200
angle = 360 / 3

for i in range(3):
    forward(side_length)
    left(angle)

mainloop()
