#include<stdio.h>

int main()
{
  int cases,i=0,stime,studs,thres;
  scanf("%i",&cases);
  for(int a=1;a<=cases;a++)
  {
    scanf("%i %i",&studs,&thres);
    for(int b=1;b<=studs;b++)
    {
      scanf("%i",&stime);
      if(stime>thres)
        i=1;
    }
    if(i==0)
    {
      printf("NO\n");
    }
    else
    {
     printf("YES\n");
    }
  }
}
