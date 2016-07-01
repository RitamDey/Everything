#include<stdio.h>

int main()
{
  char *s="hello\0";
  for(;*s='\0';s++)
   printf("%s",*s);
  return 0;
}
