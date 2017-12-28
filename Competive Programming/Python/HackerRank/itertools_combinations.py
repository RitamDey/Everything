from itertools import combinations

string, part = input().strip().split()
part = int(part)
string = sorted(string)
curr = 1

while curr <= part:
  for r in combinations(string, curr):
    print(*r, sep='')
  curr += 1

