#include<stdio.h>

int main()
{
 int ad,ay,am;
 scanf("%i",&ad);
 ay=(int)ad/365;//Calcuate the age in years
 ad%=365;//similar to ad=ad-(ay*365)
 am=(int)ad/30;//Calculates the age in months
 ad%=30;//similar to ad=ad-(ay*365) Also this line stores the reaming days
 printf("%i ano(s)\n%i mes(es)\n%i dia(s)\n",ay,am,ad);
 return 0;
}
