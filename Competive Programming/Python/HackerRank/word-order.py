from collections import OrderedDict


od = OrderedDict()
items = 0


for _ in range(int(input().strip())):
    sen = input().strip()
    try:
        od[sen] += 1
    except:
        od[sen] = 1
        items += 1


print(items)
for count in od:
    print(od[count], end=" ")

