# Subsetting a 2D NumPy array
import numpy as np

array = [
          ["a", "b"],
          ["c", "d"],
          ["e", "f"],
          ["g", "h"]
        ]

array = np.array(array)
print("Array is:", array)


# Getting a row
print("Second row is:", array[2])

# Selecting the entire second column
print("Second column is", array[:, 1])

# Selecting 5th element
print("5th element:", array[2, 1])
