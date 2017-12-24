_, init_max = map(int, input().split())
max_hurdle = max(map(int, input().split()))


diff = max_hurdle - init_max


if diff > 0:
    print(diff)
else:
    print(0)
