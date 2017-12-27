def quartile(arr , length):
    if length%2 == 1:
        return arr[(length//2)]  # Since the int divison floors the value
    else:
        x1 = length//2
        x2 = x1-1 
        return (arr[x1]+arr[x2])//2


def split(arr, length, pivot):
    lower = []
    lower_length = 0
    upper = []
    upper_length = 0

    for i in arr:
        if i < pivot:
            lower.append(i)
            lower_length += 1
        elif i > pivot:
            upper.append(i)
            upper_length += 1

    return lower, lower_length, upper, upper_length


if __name__ == '__main__':
    length = int(input())
    arr = sorted(map(int, input().split()))

    q2 = quartile(arr, length)
    lower, l_length, upper, u_length = split(arr, length, q2)
    q1 = quartile(lower, l_length)
    q3 = quartile(upper, u_length)

    print(q1, q2, q3, sep="\n")

