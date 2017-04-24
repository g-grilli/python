#!usr/bin/env python 3
from turtle import *
side_length = 150
angle = 360 / 6

for i in range(6):
    forward(side_length)
    left(angle)

mainloop()
