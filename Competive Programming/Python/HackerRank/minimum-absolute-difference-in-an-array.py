def minimumAbsoluteDifference(arr, n):
    min_diff = abs(arr[0] - arr[1])

    for i in range(1, n - 1):
        diff = abs(arr[i] - arr[i+1])
        if diff < min_diff:
            min_diff = diff
    return min_diff


if __name__ == '__main__':
    n = int(input())
    arr = sorted(map(int, input().split()))

    print(minimumAbsoluteDifference(arr, n))

