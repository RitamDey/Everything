#include<stdio.h>

int prime(int lower,int upper)
{
  for (;lower<=upper;lower++)
  {
    int s=0;
    for(int a=1;a<=lower;a++)
    {
      if(lower%a==0)
       s++;
    }
    if(s==2)
    printf("%d\n",lower);
  }
}

int main()
{
  int prime(int,int);
  int limit;
  scanf("%d",&limit);
  for(int a=1,l,u;a<=limit;a++)
  {
    scanf("%d %d",&l,&u);
    printf("\n");
    prime(l,u);
    printf("\n");
  }
  return 0;
}
