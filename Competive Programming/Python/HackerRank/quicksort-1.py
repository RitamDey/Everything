def partition(arr):
    left = []
    right = []
    equal = []
    p = arr[0]

    for x in arr:
        if x < p:
            left.append(x)
        elif x > p:
            right.append(x)
        else:
            equal.append(x)

    print(*(left + equal + right))


if __name__ == '__main__':
    int(input())
    arr = list(map(int, input().split()))
    partition(arr)
