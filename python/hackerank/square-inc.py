max_tansactions = int(input())

transactions  = list(map(int, input().split()))

for _ in range(int(input())):
    target = int(input())
    tmp = 0
    for pos in range(max_tansactions):
        tmp += transactions[pos]
        if tmp >= target:
            print("Completed at", pos+1)
            break
        elif pos == max_tansactions-1:
            print(-1)
