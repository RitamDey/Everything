def GetUnique(arr):
    unique = arr[0]

    for i in arr[1:]:
        unique ^= i

    return unique


if __name__ == '__main__':
    input()

    print(GetUnique(list(map(int, input().split()))))

