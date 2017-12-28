from collections import deque
from sys import exit


def add():
    global monk_bag, harry_bag, max_cost
    cost = harry_bag.popleft()
    monk_bag["len"] += 1
    monk_bag["cost"] += cost
    monk_bag["bag"].append(cost)

    return monk_bag["cost"] == max_cost


def remove():
    global monk_bag
    c = monk_bag["bag"].pop()
    monk_bag["cost"] -= c
    monk_bag["len"] -= 1


if __name__ == "__main__":
    _ = input()
    global harry_bag, max_cost, monk_bag
    has_fulfiled = False
    monk_bag = {'bag': deque(), "cost": 0, "len": 0}
    harry_bag = deque(map(int, input().split()))
    sen, max_cost = map(int, input().strip().split())

    for _ in range(sen):
        cmd = input()

        if cmd == "Harry":
            if add():
                print(monk_bag["len"])
                exit(0)
        else:
            remove()
    if not has_fulfiled:
        print(-1)
