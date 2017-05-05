#include<stdio.h>

int main()
{
  int cases,tstuds,rstuds,i=0;
  scanf("%i",&cases);
  for(int a=1;a<=cases&&scanf("%i %i",&tstuds,&rstuds);a++)
  {
    int time;
    for(int b=1;b<=tstuds&&scanf("%i",&time);b++)
    {
      if(time<=0)
       i++;
    }
    if(i==rstuds)
     printf("NO\n");
    else
     printf("YES\n");
    i=0;
  }
  return 0;
}
