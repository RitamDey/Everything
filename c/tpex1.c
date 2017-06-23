#include<stdio.h>

int main()
{
 int var1;
 char var2[10];
 printf("Address of var1 %x\n",&var1);
 printf("Address of array var2 %x\n",var2);
 printf("Address of 5th value in array var2 %x\n",&var2[5]);
 return 0;
}
