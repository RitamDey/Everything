#include<stdio.h>

int palin(int n)
{
 int orig=n,rev=0;
 while(n)
 {
  int x=n%10;
  rev=rev*10+x;
  x/=10;
 }
 if(orig==rev)
  return 1;
 else
  return 0;
}

int main()
{
 int cases;
 scanf("%d",&cases);
 int num;
 scanf("%d",&num);
 for(int a=num;a>=0;a++)
 {
  printf("%i ",a);
  if(palin(a))
  {
   printf("%i",a);
   break;
  }
 }
 return 0;
}

