for _ in range(int(input())):
    _, min_studs = map(int, input().split())
    studs = list(map(
                    lambda time: int(time) <= 0,
                    input().split()
                    )).count(True)

    if studs >= min_studs:
        print("NO")
    else:
        print("YES")

