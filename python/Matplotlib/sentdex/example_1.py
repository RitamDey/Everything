import matplotlib.pyplot as plt
from random import randint


size = randint(0, 10)
x = [randint(0, 100) for _ in range(size)]
y = [randint(0, 100) for _ in range(size)]
plt.plot(x, y)
plt.show()
