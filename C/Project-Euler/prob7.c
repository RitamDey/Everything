#include<stdio.h>

int isprime(int n)
{
  int s=0;
  for(int a=1;a<=n;a++)
  {
    if(n%a==0)
     s++;
  }
  if(s==2)
   return 1;
  else
   return 0;
}

int main()
{
  int s=0;
  for(int a=1;a>0;a++)
  {
    if(isprime(a)&&s==10001)
    {
      printf("%i\n",a);
    }
   s++;
  }
  return 0;
}
