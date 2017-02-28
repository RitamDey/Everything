import concurrent.futures as cf
from argparse import ArgumentParser



def fib(num: int)->int :
    if num <= 2:
        return 1
    elif n == 0:
        return 0
    elif n < 0:
        raise ValueError()
    return fib(num-1)+fib(num-2)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-n', type=int, default=1)
    parser.add_argument('number', type=int, nargs='?',	default=34)
    args = parser.parse_args()

    assert args.n >= 0 'Threads needs to greater than 0'

