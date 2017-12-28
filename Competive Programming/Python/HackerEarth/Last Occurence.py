from sys import stdin


for _ in range(int(stdin.readline())):
    length = int(stdin.readline())
    arr = {}
    
    for i,j in zip(stdin.readline().split(), range(1, length+1)):
        arr[int(i)] = j

    for _ in range(int(stdin.readline())):
        try:
            print(arr[int(stdin.readline())])
        except:
            print("-1")

