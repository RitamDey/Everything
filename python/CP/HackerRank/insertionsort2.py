def insertion_sort(arr, length):

    for y in range(1, length):
        e = arr[y]
        x = y

        while (x>0) and (arr[x-1] > e):
            arr[x] = arr[x-1]
            x -= 1

        arr[x] = e
        print(*arr)


length = int(input())
arr = list(map(int, input().split()))
insertion_sort(arr, length)

