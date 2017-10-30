from collections import defaultdict


dd = defaultdict(list)


a, b = map(int, input().strip().split())


for index in range(1, a+1):
    dd[input().strip()].append(index)


for _ in range(b):
    index = dd[input().strip()]

    if index:
        print(*index)
    else:
        print(-1)


