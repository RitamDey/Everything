l=list()
n=input()
m=map(int,input().split())
for a in m:
  l.append(a)
l=sorted(l)
max=l[0]
for a in l:
  if(max>a):
    print(a)
    break

