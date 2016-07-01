#include<stdio.h>
int main()
{
  int s=0,s1=1,ts=0;
  while(1)
  {
    int t=s+s1;
    s=s1;
    s1=t;
    if(!(t%2))
    {
     ts+=t;
     if(t>4000000)
     {
      ts-=t;
      break;
     }
    }
  }
  printf("%i\n",ts);
return 0;
}

