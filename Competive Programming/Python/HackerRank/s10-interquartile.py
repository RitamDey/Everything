def median(arr, length):
    if length%2 == 0:
        x1 = length//2
        x2 = x1 - 1
        return (arr[x1]+arr[x2])/2
    else:
        return arr[length//2]


_ = input()
a = map(int, input().split())
f = map(int, input().split())
arr = []
length = 0


for i,j in zip(a, f):
    arr += [i]*j
    length += j

arr = sorted(arr)
lower, upper = [], []

if length%2 == 0:
    lower = arr[:(length//2)]
    upper = arr[(length//2):]
else:
    lower = arr[:(length//2)+1]
    upper = arr[(length//2)+1:]


print("%.1f" %abs(median(lower, len(lower)) - median(upper, len(upper))))

