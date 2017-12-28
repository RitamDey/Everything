def sort(arr, length):
    for _ in range(length):
        for i in range(length-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


def search(arr, low, high, key):
    if low > high:
        return None

    mid = (low+high) // 2

    if arr[mid] == key:
        return mid
    elif key > arr[mid]:
        return search(arr, mid+1, high, key)
    else:
        return search(arr, low, mid-1, key)



case_count = 1
while True:
    n, q = map(int, input().split())

    if n == 0 and q == 0:
        break

    print("CASE#", case_count)
    case_count += 1
    arr = sort([int(input()) for _ in range(n)], n)

    for _ in range(q):
        k = int(input())
        pos = search(arr, 0, n, k)

        if pos is None:
            print(k, "not found")
        else:
            print(k, "found at", pos+1)

