def rev(a):
    sn=0
    while a!=0:
     sn=sn*10+(a%10)
     a=int(a/10)
    return(sn)
def count(s):
 for n in s:
  print("%s %s" %(n,s.count(n)))
def prime(n):
     s=0
     for a in range(1,n+1):
         if(n%a==0):
          s+=1
     if s==2:
         return n
     else:
         return 0
def composite(n):
     s=0
     for a in range(1,n+1):
         if(n%a==0):
          s+=1
     if s==2:
         return 0
     else:
         return n
