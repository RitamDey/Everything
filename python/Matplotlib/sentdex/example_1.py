import matplotlib.pyplot as plt
from numpy.random import randint, random


size = randint(10)
x = [random() for _ in range(size)]
y = [random() for _ in range(size)]
plt.plot(x, y)
plt.show()
