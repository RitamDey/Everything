""" Histogram example """
import matplotlib.pyplot as plt
from numpy import random

population_ages = [random.randint(low=20, high=130) for _ in range(40)]
bins = list(range(0, 135, 10))


plt.hist(population_ages, bins, histtype='bar')
plt.xlabel('Population Ages')
plt.ylabel('Population Group')
plt.show()
