cases = int(input())
count = 0
chocs = list(map(int, input().split()))
n_sum, n_parts = map(int, input().split())


for i in range(cases):
    if sum(chocs[i:i+n_parts]) == n_sum:
        count += 1


print(count)
