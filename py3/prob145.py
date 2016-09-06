from mylib import rev

case=int(input())

for a in range(case):
 c=0
 test=int(input())
 for b in range(1,test+1):
  if (b+rev(b))!=0:
   c+=1

 print(c)
