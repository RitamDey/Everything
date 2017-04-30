from threading import Thread
from os import cpu_count
import argparse


def fib(n):
    if n <= 2:
        return 1
    elif n == 0:
        return 1
    return fib(n-1)+fib(n-2)


def fact(n):
    if n <= 0:
        return 1
    return n*fact(n-1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', type=str, default="fib", help="fibonacci or factorial")
    parser.add_argument('number', type=int, default=50)
    args = parser.parse_args()

    if args.c == 'fact':
        callback = fact
    else:
        callback = fib

    for i in range(cpu_count()):
        t = Thread(target=callback, args=(args.number,))
        t.start()

