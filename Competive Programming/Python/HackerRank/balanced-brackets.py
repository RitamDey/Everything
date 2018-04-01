from collections import deque


pairs = {')': '(', ']': '[', '}': '{'}


def isBalanced(s):
    q = deque()

    for c in s:
        if c in pairs.keys():
            try:
                if q.pop() != pairs[c]:
                    return "NO"
            except IndexError:
                return "NO"

        q.append(c)
    return "YES" if not q else "NO"


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        s = input().strip()
        print(isBalanced(s))

