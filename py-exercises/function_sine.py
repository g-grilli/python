#!usr/bin/env python 3
import matplotlib.pyplot as plot
import math
def sine(x):
    return math.sin(x)
xs = list(range(-5, 5, 1))
ys =[]
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()

if __name__ == "__main__":
    sine(x)

# Write a function f(x) that returns the sin of x. Hint: there is a sin function
# in the math module. Plot it from -5 to 5 in increments of 1. It should look
# like this Sin 1
