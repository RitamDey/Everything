fans, n_fans = map(int, input().split())
fans_dict = [input().split() for _ in range(fans)]


sorted = False
while not sorted:
    for i in range(fans-1):
        sorted = True
        if fans_dict[i][1] < fans_dict[i+1][1]:
            fans_dict[i], fans_dict[i+1] = fans_dict[i+1], fans_dict[i]
            sorted = False


for x in range(n_fans):
    print(fans_dict[x][0])
