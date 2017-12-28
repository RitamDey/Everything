def f(x, y):
    if not x:
        return y+1
    elif x and not y:
        return f(x-1, 1)
    else:
        return f(x-1, f(x, y-1))


if __name__ == '__main__':
    k = map(int, input().split())
    print(f(*k))