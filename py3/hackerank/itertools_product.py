from itertools import product

list1 = map(int, input().split())
list2 = map(int, input().split())

products=product(list1, list2)

print(*sorted(products))
