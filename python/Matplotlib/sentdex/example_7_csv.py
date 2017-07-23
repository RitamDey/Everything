""" Loading data from files """
import matplotlib.pyplot as plt
import csv


x = []
y = []


with open('example.csv', 'r') as file:
    plots = csv.reader(file, delimiter=',')
    print(plots)
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x, y, label='Loaded from file')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Random Graph')
plt.show()
