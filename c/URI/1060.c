#include<stdio.h>

int main()
{
 float n;
 int total=0,a;
 for(a=1;a<=6;a++)
 {
  scanf("%f",&n);
  if(n>0)
   total++;
 }
 printf("%i valores positivos\n",total);
 return 0;
}

