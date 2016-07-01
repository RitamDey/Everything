#include<stdio.h>

int main()
{
 float num,avg,a;
 int total;
 avg=total=0;
 for(a=1;a<=6;a++)
 {
  scanf("%f",&num);
  if(num>0)
  {
   avg+=num;
   total++;
  }
 }
 printf("%i valores positivos\n%.1f\n",total,avg/total);
 return 0;
}
