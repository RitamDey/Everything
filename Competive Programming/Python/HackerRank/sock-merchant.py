def pair_up(shoes):
    d = {}
    for i in shoes:
        try:
            d[i] += 1
        except KeyError:
            d[i] = 1
    return d


def count(pairs):
    count = 0
    for i in pairs:
        count += pairs[i]//2

    return count


_ = int(input())
print(count(pair_up(map(int, input().split()))))
