length = int(input())
transactions = list(map(int, input().split()))


for _ in range(int(input())):
    target = int(input())
    s = 0
    for i in range(length):
        s += transactions[i]
        if s >= target:
            print(i+1)
            break
    else:
        print(-1)

