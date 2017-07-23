""" Working with CSV using NumPy """
import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('example.csv',
                  delimiter=',',
                  unpack=True,
                  dtype=int
                  )

plt.plot(x, y, label='Loaded from file')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Random Graph')
plt.show()
