#include<stdio.h>

int main()
{
 int t,c,k,w;
 scanf("%i",&t);
 for(int a=1;a<=t&&scanf("%i %i %i",&c,&k,&w);a++)
 {
  if((c*w)<=k)
   printf("YES\n");
  else
   printf("NO\n");
 }
 return 0;
}
