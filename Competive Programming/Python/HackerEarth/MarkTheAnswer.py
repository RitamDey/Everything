_, max_difficulty = map(int, input().split())

questions = [int(num) for num in input().split()]
count = 0
skip = 0

for question in questions:
    if skip < 2:
        if question < max_difficulty:
            count += 1
        else:
            skip += 1

print(count)