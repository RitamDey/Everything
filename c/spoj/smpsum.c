#include<stdio.h>
int main()
{
  int s=0,n1,n2;
  scanf("%i %i",&n1,&n2);
  for(int a=n1;a<=n2;a++)
   s+=(a*a);
  printf("%i\n",s);
  return 0;
}
