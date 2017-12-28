"""
The identity tool returns an identity array. An identity array is a square matrix with all the main diagonal elements
as 1 and the rest as 0. The default type of elements is float.
"""
"""
The eye tool returns a 2-D array with 1's as the diagonal and 0's elsewhere. The diagonal can be main, upper
or lower depending on the optional parameter k.
A positive k is for the upper diagonal, a negative k is for the lower, and a 0 (default) is for the main diagonal.
"""
from numpy import eye


x, y = map(int, input().strip().split())


arr = eye(x, y)
print(arr)
