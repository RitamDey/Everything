from itertools import accumulate


def pow(base=2, n=1000):
    if n <= 0:
        return 1
    res = pow(n=n//2)

    if n%2 == 1:
        return base * res * res
    else:
        return res * res


print(sum([int(n) for n in str(pow())]))
