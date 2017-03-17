#include<stdio.h>
int rev(int);
int main()
{
 int c,n1,n2;
 scanf("%i",&c);
 for(int a=1;a<=c&&scanf("%i %i",&n1,&n2);a++)
 {
  n1=rev(n1);
  n2=rev(n2);
  int s=rev(n1+n2);
  printf("%i\n",s);
 }
 return 0;
}
int rev(int n)
{
 int s=0;
 while(n)
 {
  int x=n%10;
  s=s*10+x;
  n/=10;
 }
 return s;
}
