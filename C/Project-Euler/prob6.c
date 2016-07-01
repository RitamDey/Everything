#include<stdio.h>
int main()
{
 int s=0,ss=0;
 for(int a=1;a<=100;a++)
 {
  s+=a;
  ss+=(a*a);
 }
 s*=s;
 printf("%i\n",s-ss);
 return 0;
}
