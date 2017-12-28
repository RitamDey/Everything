def insertion_sort(arr, length):
    e = arr[-1]
    x =  length - 1

    while (x>0) and (arr[x-1] > e):
        arr[x] = arr[x-1]
        x -= 1
        print(*arr)
    arr[x] = e
    print(*arr)


length = int(input())
arr = list(map(int, input().split()))
insertion_sort(arr, length)

