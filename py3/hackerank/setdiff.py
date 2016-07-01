s1=set()
s2=set()
n=input()
m=map(int,input().split())
for a in m:
    s1.add(a)
n=input()
m=map(int,input().split())
for a in m:
    s2.add(a)
r=s1-s2
r.update(s2-s1)
print(sorted(list(r)))
