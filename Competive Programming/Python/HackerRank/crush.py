import itertools

n, ops = map(int, input().split())

the_list = [0,]*n

for _ in range(ops):
    a, b, k = map(int, input().split())
    for pos in range(a-1, b):
        the_list[pos] += k

print(list(itertools.accumulate(the_list, max)))