def count_birds(birds):
    most_birds = (6, 0)

    for i in [1, 2, 3, 4, 5]:
        c = birds.count(i)
        if c > most_birds[-1]:
            most_birds = (i, c)
        elif c == most_birds[-1] and i < most_birds[0]:
            most_birds = (i, c)
    return most_birds[0]


if __name__ == '__main__':
    input()
    birds = list(map(int, input().split()))

    print(count_birds(birds))

