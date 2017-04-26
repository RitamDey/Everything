from numpy import array, ceil, floor, rint


arr = array(input().strip().split(), float)


print(floor(arr))  # Rounds down every element to the nearest integer
print(ceil(arr))  # Rounds up each element to the upper whole intger
print(rint(arr))  # Rounds every elements
