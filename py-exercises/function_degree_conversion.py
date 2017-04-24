#!usr/bin/env python 3
import matplotlib.pyplot as plot

def convert(x):
    return x * 1.8 + 32
xs = list(range(0, 50, 1))
ys =[]
for x in xs:
    ys.append(convert(x))
plot.plot(xs, ys)
plot.ylabel('Temperature F')
plot.ylabel('Temperature C')
plot.show()

if __name__ == "__main__":
    convert(x)

# Write a function that takes a temperature in Celcius and converts it
# Fahrenheit. Plot it on a graph.
