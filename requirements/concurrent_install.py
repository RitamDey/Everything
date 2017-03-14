from concurrent.futures import ThreadPoolExecutor as threads
from collections import deque
from sys import stdin, argv


stack = deque()

def parse_file(fname=stdin):
    for line in fname.readlines():
        if line.startswith('#'):continue
        stack.append(line)
    fname.close()


if __name__ == '__main__':
    parse_file(open(argv[1], 'r'))

    for name in stack:
        print(name)
