#include<stdio.h>
int main()
{
  unsigned int sum=0;
  for(int  a=1;a<1000;a++)
  {
    if((a%3==0)||(a%5==0))
     sum+=a;
  }
printf("%d\n",sum);
}
