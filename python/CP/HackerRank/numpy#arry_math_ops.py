from numpy import array
from numpy import add, subtract as sub, multiply as mul
from numpy import divide as div, mod, power as pow

n, _ = map(int, input().strip().split())


arr1 = array([input().strip().split() for _ in range(n)], int)
arr2 = array([input().strip().split() for _ in range(n)], int)


print(add(arr1, arr2))
print(sub(arr1, arr2))
print(mul(arr1, arr2))
print(arr1 // arr2)
print(mod(arr1, arr2))
print(pow(arr1, arr2))
