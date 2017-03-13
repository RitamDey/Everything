l=list()
n=input()
l=sorted(map(int,input().split()))
max=l[0]
for a in l:
  if(max>a):
    print(a)
    break

