data = int(input().split()[1])

marks = [map(float, input().split()) for _ in range(data)]

for s in zip(*marks):
  avg = sum(s)/data
  print(avg)

