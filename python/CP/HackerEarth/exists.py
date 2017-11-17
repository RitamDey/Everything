for _ in range(int(input())):
    l = int(input())

    arr = [None]*l
    for i in input().split():
        pos = (hash(i) // l) % l
        if arr[pos] is not None:
            arr[pos] = (*arr[pos], i)
        else:
            arr[pos] = (i,)


    for _ in range(int(input())):
        key = input()
        pos = (hash(key) // l) % l
        print("Yes" if arr[pos] and key in arr[pos] else "No")

