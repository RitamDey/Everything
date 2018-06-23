_, n_people = map(int, input().split())
flowers = sorted(map(int, input().split()), reverse=True)

c = 0
profit = 0


while flowers:
    for _ in range(n_people):
        if flowers:
            profit += (c + 1) * flowers.pop(0)
        else:
            break

    c += 1


print(profit)
