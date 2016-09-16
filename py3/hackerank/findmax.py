data = []
for _ in range(int(input())):
    ins = input().split()
    if ins[0] == '1':
        new_value = int(ins[1])
        if data and new_value < data[-1]:
            new_value = data[-1]
        data.append(new_value)
    elif ins[0] == '2':
        data.pop()
    elif ins[0] == '3':
        print(data[-1])
