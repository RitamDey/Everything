#include<stdio.h>

int main()
{
 float time,speed;
 scanf("%f %f",&time,&speed);
 printf("%.3f\n",((speed*time)/12.0));//To Ensure that the final result is in floating point when allint input is give like the one in sample input 1
 return 0;
}
