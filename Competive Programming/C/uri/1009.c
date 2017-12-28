#include<stdio.h>

int main()
{
 char s[15];
 float fs,ts;
 fgets(s,15,stdin);
 scanf("%f %f",&fs,&ts);
 printf("TOTAL = R$ %.2f\n",fs+((ts*15)/100));
 return 0;
}
