""" Bar Charts """
import matplotlib.pyplot as plt

x = [2, 4, 6, 8, 10]
y = [6, 7, 8, 2, 4]

x2 = [1, 3, 5, 7, 9]
y2 = [7, 8, 2, 4, 2]

plt.bar(x, y, label='Bar Graph 1', color='red')
plt.bar(x2, y2, label='Bar Graph 2', color='cyan')

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title('Random Graph\nEverything Random.')
plt.legend()
plt.show()
