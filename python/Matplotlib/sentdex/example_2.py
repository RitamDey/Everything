""" Legends titles and labels """
import matplotlib.pyplot as plt
from numpy import random


size = random.randint(20)
x = [random.random() for _ in range(size)]
y = [random.random() for _ in range(size)]
print(f'X list: {x}\nY list: {y}')

plt.plot(x, y)

# Set labels to axis
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Random Graphs.\nEverything is random.')

plt.show()
