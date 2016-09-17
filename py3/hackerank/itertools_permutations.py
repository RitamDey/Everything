from itertools import permutations

string,length = input().split()
result = sorted(list(permutations(string, int(length))))

for r in result:
  print(*r, sep='')
