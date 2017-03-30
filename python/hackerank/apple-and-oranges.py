s, t = map(int, input().split())
a, b = map(int, input().split())

input()

apples = 0
apples_dist = map(int, input().split())

for apple in apples_dist:
    if apple+a >= s:
        apples += 1

oranges = 0
oranges_dist = map(int, input().split())

for orange in oranges_dist:
    if orange+b <= t:
        oranges += 1


print(apples, oranges, sep='\n')
