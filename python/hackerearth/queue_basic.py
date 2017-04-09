from collections import deque


max_len = int(input())
queue = deque(maxlen=max_len)


for _ in range(max_len):
    op = input().split()
    if op[0] == 'E':
        queue.appendleft(int(op[1]))
        print(len(queue))
    else:
        try:
            print(queue.pop(), len(queue))
        except IndexError:
            print(-1, 0)

