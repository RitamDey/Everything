from collections import deque


def max_chute(chutes):
    max_chute = 0
    max_chip = chutes[max_chute][-1]

    #print(chutes[max_chute])
    for chute in range(1, len(chutes)):
        #print(chutes[chute][-1], chutes[max_chute][-1])
        if chutes[chute][-1] > max_chip:
            max_chute = chute
            max_chip = chutes[chute][-1]
    #print("Max chute ", chutes[max_chute])

    return max_chute


n_chutes, n_chips = map(int, input().split(","))

chutes = []

for _ in range(n_chutes):
    obj = deque(map(int, input().split(",")), maxlen=n_chips)
    chutes.append(obj)

#print(chutes)

number = 0


while chutes:
    max_chute_index = max_chute(chutes)
    number = number*10 + chutes[max_chute_index].pop()

    if not chutes[max_chute_index]:
        chutes.pop(max_chute_index)


print(number)
