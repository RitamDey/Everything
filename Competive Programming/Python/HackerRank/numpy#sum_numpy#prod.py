from numpy import array


n, _ = map(int, input().strip().split())
arr = array([input().strip().split() for _ in range(n)], int)


print(arr.sum(axis=0).prod())
