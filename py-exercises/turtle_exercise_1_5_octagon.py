#!usr/bin/env python 3
from turtle import *
side_length = 100
angle = 360 / 8

for i in range(8):
    forward(side_length)
    left(angle)

mainloop()
