#include<stdio.h>

int main()
{
 int num,total=0,a;
 for(a=1;a<=5;a++)
 {
  scanf("%i",&num);
  if(!(num%2))
  total++;
 }
 printf("%i valores pares\n",total);
 return 0;
}
