def count_ones(n):
    count = 0
    while n:
        n = n&(n-1)
        count += 1
    return count


while True:
    try:
        print(count_ones(int(input())))
    except EOFError:
        break

