#include<stdio.h>
int main()
{
  int s=0,s1=1,t;
  for(int a=1;a<=10;a++)
  {
    t=s+s1;
    s=s1;
    s1=t;
    printf("%d ",t);
  }
}
