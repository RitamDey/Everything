""" Pie Chart """
import matplotlib.pyplot as plt


days = list(range(1, 6))
sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

slices = [7, 2, 2, 13]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'b']

plt.pie(
    slices,
    labels=activities,
    colors=cols,
    startangle=90,
    shadow=True,
    explode=[0.2, 0.1, 0.05, 0.5],
    autopct='%1.1f%%'  # this is used to show percentage
)

plt.title('Random Pie Chart')
plt.show()
