#include<stdio.h>

int main()
{
 int dist;
 float fuel;
 scanf("%i %f",&dist,&fuel);
 printf("%.3f km/l\n",(dist/fuel));
 return 0;
}
