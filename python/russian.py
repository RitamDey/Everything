def russian(x, y):
    z = 0
    while x != 0:
        if x%2 == 1:
            z += y
        y = y << 1
        x = x >> 1
    return z

if __name__ == '__main__':
    print(russian(int(input()), int(input())))
