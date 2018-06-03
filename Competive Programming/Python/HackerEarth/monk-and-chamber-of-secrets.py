from collections import deque


if __name__ == '__main__':
    n, x = map(int, input().split())
    queue = deque(map(int, input().split()))

    for _ in range(x):
        
