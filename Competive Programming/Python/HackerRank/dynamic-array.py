lastAns = 0

n, queries = map(int, input().split())

seqlist = [[] for _ in range(n)]

for _ in range(queries):
    query = list(map(int, input().split()))
    ans = (int(query[1]) ^ lastAns) % n
    # print('Calculaion now', ans)

    if query[0] == 1:
        seqlist[ans].append(int(query[2]))
        # print('Current list', seqlist)
    
    elif query[0] == 2:
        # print(seqlist[ans])
        lastAns = seqlist[ans][int(query[2])%len(seqlist[ans])]
        print(lastAns)