#include<stdio.h>

int main()
{
 int test;
 scanf("%i",&test);
 for(int a=1;a<=test;a++)
 {
  long int  n1,n2;
  scanf("%ld %ld",&n1,&n2);
  printf("%lu\n",n1*n2);
 }
 return 0;
}
