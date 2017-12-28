from numpy import array, concatenate


arr1, arr2 = [], []
n, m, _ = input().strip().split()


for _ in range(int(n)):
    arr1.append(input().strip().split())


for _ in range(int(m)):
    arr2.append(input().strip().split())


arr1, arr2 = array(arr1, int), array(arr2, int)
arr = concatenate((arr1, arr2), axis=0)


print(arr)
