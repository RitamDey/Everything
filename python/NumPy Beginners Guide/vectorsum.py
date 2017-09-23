import sys
from datetime import datetime
import numpy as np


"""
Chapter 1 of NumPy Beginners Guide.
This program demonstrates vector addition the Python way.
Run from the command line as follows

python3 vectorsum.py n

where n is an integer that specifies the size of the vectors.

The first vector to be added contains the squares of 0 up to n.
The second vector contains the cubes of 0 up to n.
The program prints the last 2 elements of the sum and the elapsed
time.
"""


def NumPySum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b

    return c


def PythonSum(n):
    a = list(range(n))
    b = list(range(n))
    c = []

    for i in range(n):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b[i])

    return c


def run(func):
    size = int(sys.argv[1])
    start = datetime.now()
    c = func(size)
    delta = datetime.now() - start
    print("The last 2 elements of the sum", c[-2:])
    print("{0} elapsed time {1}".format(func.__name__, delta.microseconds))


run(PythonSum)
run(NumPySum)
