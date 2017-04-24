#!usr/bin/env python 3
from numpy import arange
import matplotlib.pyplot as plot
import math
def sine(x):
    return math.sin(x)
xs = list(arange(-5, 5, 0.1))
ys =[]
for x in xs:
    ys.append(sine(x))

plot.plot(xs, ys)
plot.show()

if __name__ == "__main__":
    sine(x)
# Unfortunately, that looked horrible, and we can't use smaller increment values
# because the range function only supports integers. Fortunately, there is a
# Python package called numpy that will allow ranges with decimal-point
# increments. You will install it using the command pip install numpy.
# Once you've done that, you write the import statement: from numpy import
# arange, and then you can use arange in place of range to use decimal
# increments, like so:

# xs = arange(-5, 6, 0.1)
# Now plot the graph from -5 to -5 in 0.1 increments, and you should see this
