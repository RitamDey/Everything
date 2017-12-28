for _ in range(int(input())):
    h_init = 1
    for season in range(int(input())):
        if season%2:
            h_init += 1
        else:
            h_init *= 2
    print(h_init)

