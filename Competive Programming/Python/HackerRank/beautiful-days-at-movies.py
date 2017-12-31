def rev(n):
    r = 0
    while n:
        r = r*10 + n%10
        n = n//10
    return r


date1, date2, k = map(int, input().split())


count = 0
for date in range(date1, date2+1):
    if abs(date - rev(date))%k == 0:
        count += 1
print(count)

