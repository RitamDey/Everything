def cheapest_subarray(arr, length):
    min_cost = arr[0] + arr[1]

    for i in range(length - 1):
        cost = arr[i] + arr[i+1]
        if cost < min_cost:
            min_cost = cost

    return min_cost


if __name__ == "__main__":
    for _ in range(int(input())):
        length = int(input())
        arr = list(map(int, input().split()))

        print(cheapest_subarray(arr, length))

