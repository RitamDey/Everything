_, tests = input().split()
numbers = list(map(int, input().split()))

for _ in range(int(tests)):
    instruct= list(map(int, input().split()))
    if instruct[0] == 1:
        numbers[instruct[1]] = 1 - numbers[instruct[1]]
    else:
        total = sum(numbers[instruct[1]:instruct[2]+1])
        if total%2:
            print("ODD")
        else:
            print("EVEN")
