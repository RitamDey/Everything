def derangment(n):
    if n == 0:
        return 1

    if n == 1:
        return 0

    return (n-1) * (derangment(n-1) + derangment(n-2))


if __name__ == '__main__':
    print(derangment(int(input())))

