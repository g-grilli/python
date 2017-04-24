#!usr/bin/env python 3
import matplotlib.pyplot as plot

def odd_or_even(x):
    nums = x % 2
    if nums == 0:
        return -1
    else:
        return 1
xs = list(range(-5, 5, 1))
ys =[]
for x in xs:
    ys.append(odd_or_even(x))

plot.bar(xs, ys)
plot.show()

if __name__ == "__main__":
    odd_or_even(x)

# Write a function f(x) that returns 1 if x is odd and -1 if x is even.
#Plot it for x values of -5 to 5 in increments of 1.
#This time, instead of using plot.plot, use plot.bar instead to make a bar graph.
#It should look like:
plot
# -1 5 blue verticle lines
# and off set
# 1 5 blue veritcle lines
