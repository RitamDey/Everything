tests = int(input())
for _ in range(tests):
    data = [float(num) for num in input().split()]
    sum = 2*data[0]+3*data[1]+5*data[2]
    print("%0.1f" % (sum/10))
