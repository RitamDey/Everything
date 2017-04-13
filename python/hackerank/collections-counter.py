from collections import Counter

def read():
    return map(int, input().strip().split())

_ = input()
shoes = Counter(read())
income = 0

for _ in range(int(input())):
    size,price = read()
    if shoes[size]:
        shoes[size] -= 1
        income += price

print(income)
