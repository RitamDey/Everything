""" Legends titles and labels """
import matplotlib.pyplot as plt
from numpy import random


size = random.randint(20)
x = [random.random() for _ in range(size)]
y = [random.random() for _ in range(size)]
x2 = [e * random.random() for e in x]
y2 = [e * random.random() for e in y]

plt.plot(x, y, label='Plot 1')
plt.plot(x2, y2, label='Plot 2')

# Set labels to axis
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Random Graphs.\nEverything is random.')
plt.legend()

plt.show()
