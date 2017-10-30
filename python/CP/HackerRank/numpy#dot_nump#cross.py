from numpy import array, cross, dot


n = int(input().strip())


arr1 = array([input().strip().split() for _ in range(n)], int)
arr2 = array([input().strip().split() for _ in range(n)], int)


print(dot(arr1, arr2))
print(cross(arr1, arr2))
