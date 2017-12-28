#include<stdio.h>
int main()
{
 int s=0;
 for(unsigned long int a=1;a>0;a++)
 {
  for(int b=1;b<=20;b++)
  {
   if(a%b==0)
    s++;
  }
  if(s==20)
  {
   printf("%lu\n",a);
   break;
  }
  s=0;
 }
 return 0;
}
