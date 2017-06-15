def wrapper(f):
    def fun(l):
        x = []
        for num in l:
            if len(num) == 10:
                x.append("+91 %s %s" %(num[:5], num[5:]))
            elif len(num) == 12:
                x.append("+91 %s %s" %(num[2:7], num[7:]))
            elif len(num) == 13:
                x.append("+91 %s %s" %(num[3:8], num[8:]))
            else:
                x.append("+91 %s %s" %(num[1:6], num[6:]))
            return f(x)
    return fun


@wrapper
def sort_phone(l):
    print('\n'.join(sorted(l)))


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)

