from itertools import combinations_with_replacement

string, part = input().strip().split()

results = combinations_with_replacement(sorted(string), int(part))

for result in results:
  print(*result, sep='')

