_, n_queries = map(int, input().split())
arr = list(map(int, input().split()))


for _ in range(n_queries):
    q_type, arg1, arg2 = map(int, input().split())

    if q_type == 1:
        arr[arg1] = arg2
    else:
        print(sum(arr[arg1:arg2+1]))

