from math import sqrt


n = int(input())
data = list(map(int, input().split()))

mean = sum(data)/n
variance = 0.0

for d in data:
    variance += (d-mean)**2
variance /= n


print(round(sqrt(variance), 1))
