""" Examples of Scatter """
import matplotlib.pyplot as plt
from numpy.random import random


x = [x / 10 for x in range(0, 11)]
y = [float(random(1)) for _ in range(11)]


plt.scatter(x, y, label='Random Scatter', marker='*', s=100)

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Random Scatter Graph")
plt.legend()
plt.show()
