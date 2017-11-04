for _ in range(int(input())):
    _, dis_count = map(int, input().split())
    x = set(map(int, input().split()))
    if len(x) == dis_count:
        print("GOOD")
    elif len(x) > dis_count:
        print("AVERAGE")
    else:
        print("BAD")

