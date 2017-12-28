cases=int(input())
for a in range(cases):
    num=input()
    if num==num[::-1]:
        print("YES")
    else:
        print("NO")
