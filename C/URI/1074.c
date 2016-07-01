#include<stdio.h>

int main()
{
 int range,n,a;
 scanf("%i",&range);
 for(a=1;a<=range;a++)
 {
  scanf("%i",&n);
  if(n==0)
   printf("NULL\n");
  else if(n>0)
  {
   if(!(n%2))
    printf("EVEN ");
   else
    printf("ODD ");
   printf("POSITIVE\n");
  }
  else
  {
   if(!(n%2))
    printf("EVEN ");
   else
    printf("ODD ");
   printf("NEGATIVE\n");
  }
  return 0;
 }
}
