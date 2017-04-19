from re import findall


for _ in range(int(input())):
    _ = input()
    print(len(findall(r'[0-9]+', input())))
