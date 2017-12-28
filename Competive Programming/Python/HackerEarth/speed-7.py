for _ in range(int(input())):
    length = int(input())
    if length == 1:
        input()
        print("1")
        continue
    speeds = list(map(int, input().split()))
    count = 0
    for i in range(length):
        runsTop = False
        for j in range(i+1, length):
            if speeds[i]  speeds[j]:
                count += 1
                break
    print(length)
