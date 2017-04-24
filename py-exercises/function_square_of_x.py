#!usr/bin/env python 3

import matplotlib.pyplot as plot

def f(x):
    return x * x

xs = list(range(-100, 100))
ys =[]
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()

if __name__ == "__main__":
    f(x)
