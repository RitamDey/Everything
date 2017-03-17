#include<stdio.h>

int rev(int n)
{
  int r=0;
  while(n)
  {
    int x=n%10;
    r=r*x;
    n/=10;
  }
  return r;
}

int main() {
  int rev(int);
  int c,t=0;
  scanf("%i",&c);
  for(int a=1,n;a<=c&&scanf("%i",&n);a++)
  {
    for(int b=1;b<=n;b++)
    {
      int r=rev(b);
      if((r+b)%2)
       t++;
    }
    printf("%i\n",t);
  }
  return 0;
}
