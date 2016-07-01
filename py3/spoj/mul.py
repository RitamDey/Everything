cases=int(input())

for a in range(cases):
    num=list()
    num=input().split(" ")
    mul=1
    for b in num:
        b=int(b)
        mul*=b
    print(mul)