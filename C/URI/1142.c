#include<stdio.h>

int main()
{
 int limit,n=1;
 scanf("%i",&limit);
 for(int a=1;a<=(limit*4);a++)
 {
  if(a%4==0)
   printf("PUM\n");
  else
   printf("%i ",n);
  n++;
 }
 return 0;
}
