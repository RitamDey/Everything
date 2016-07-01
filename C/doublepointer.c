#include<stdio.h>

int main()
{
  char a="H";
  char *b=&a;
  //char *c=&b;
  //printf(**c);
  printf("%s\n",*b);
  printf("%s\n",a);
  return 0;
}
