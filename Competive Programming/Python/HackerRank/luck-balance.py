length, k = map(int, input().split())
lucks = []
lucks_left = 0

for _ in range(length):
    l, t = map(int, input().split())

    if t == 1:
        lucks.append(l)
    else:
        lucks_left += l


lucks.sort(reverse=True)

luck_used = 0

if k >= len(lucks):
    print(lucks_left + sum(lucks))
elif k == 0:
    print(lucks_left - sum(lucks))
else:
    for i in range(k):
        luck_used += lucks.pop(0)

    print(lucks_left + luck_used - sum(lucks))

