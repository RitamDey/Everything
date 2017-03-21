stack = []

while True:
    try:
        instruction = input().split()
        if instruction[0] == "add":
            stack.append(instruction[1])
        else:
            print(stack.pop())
    except:
        break
