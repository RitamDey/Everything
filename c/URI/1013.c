#include<stdio.h>
#include<stdlib.h>
int main()
{
 int a,b,c;
 scanf("%i %i %i",&a,&b,&c);
 int max=((a+b)+abs(a-b))/2;
 int max2=((b+c)+abs(b-c))/2;
 max=((max+max2)+abs(max-max2))/2;
 printf("%i eh o maior\n",max);
 return 0;
}
