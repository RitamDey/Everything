arr_len = int(input())
arr = list(map(int, input().strip().split()))
swaps = 0


for i in range(arr_len-1):
    for j in range(arr_len-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swaps += 1


print(swaps)
