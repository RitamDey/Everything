from numpy import array


arr = []
n, _ = input().strip().split()


for _ in range(int(n)):
    arr.append(input().strip().split())


arr = array(arr, int)


print(arr.transpose())
print(arr.flatten())
