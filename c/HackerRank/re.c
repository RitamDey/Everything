#include<stdio.h>

int factorial(int);

int factorial(int n)
{
  int t=1;
  if(n>1)
   t=n*factorial(n-1);
  else
   return 1;
  return t;
}

int main()
{
  int n;
  scanf("%d",&n);
  printf("%i\n",factorial(n));
  return 0;
}
