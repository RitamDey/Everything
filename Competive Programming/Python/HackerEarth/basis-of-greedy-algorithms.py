from itertools import accumulate


for _ in range(int(input())):
    _, target = map(int, input().split())
    n_bottles = 0

    for i in accumulate(sorted(map(int, input().split()))):
        if i <= target:
            n_bottles += 1

    print(n_bottles)

