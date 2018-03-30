def rush(tm, t):
    complete = []

    for time in sorted(tm):
        if sum(complete) + time <= t:
            complete.append(time)
        else:
            break

    return len(complete)


if __name__ == '__main__':
    n, t = map(int, input().split())
    tm = []
    tm_i = 0

    for tm_i in range(n):
        tm.append(int(input()))

    result = rush(tm, t)
    print(result)

