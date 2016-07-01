#include<stdio.h>

int main()
{
  //int n[10];
  //gets(n);
  int *n;
  //scanf("%10d",n);
  gets(n);
  for(int a=0;a<10;a++)//&&scanf("%d",*n))
   printf("%d\n",n++);
  return 0;
}
