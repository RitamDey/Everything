import math


def get_divisors(n):
    divs = []

    for i in range(1, int(math.sqrt(n)+1)):
        if n%i == 0:
            if i%2:
                divs.append(i)
            if n//i != i and (n//i)%2:
                divs.append(i)
    
    return divs


if __name__ == '__main__':
    for _ in range(int(input())):
        print(sum(get_divisors(int(input()))))

