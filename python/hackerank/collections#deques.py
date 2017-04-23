from collections import deque


dq = deque()


for _ in range(int(input("Enter number of queries: "))):
    # *args will consume all the values from the 1 index
    # if there is none, the *args will have a value of []
    func, *args = input("append or appendleft or pop or popleft ").split()
    getattr(dq, func)(*args)


print(*dq)

