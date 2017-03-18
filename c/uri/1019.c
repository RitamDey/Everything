#include<stdio.h>

int main()
{
 int sec,in=3600;
 scanf("%i",&sec);
 for(int a=1;a<=2;a++)
 {
  printf("%i:",sec/in);
  sec%=in;
  in/=60;
 }
 printf("%i\n",sec);
 return 0;
}
