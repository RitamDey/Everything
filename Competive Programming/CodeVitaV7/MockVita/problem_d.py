def mul(arr):
    res = arr[0]

    for i in arr[1:]:
        res *= i

    return res


def gen_subarray(arr, n):
    for i in range(1 << n):
        y = 1
        for j in range(n):
            if i & (1 << j):
                y *= arr[j]
        yield y


def main():
    n, p1, p2 = map(int, input().split(","))
    arr = list(map(int, input().split(",")))

    obj = gen_subarray(arr, n)
    count = 0

    for i in obj:
        if i % (p1 * p2) == 0:
            count += 1

    print(count % 1009)


main()
