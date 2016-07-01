#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int main()
{
  float x1,x2,y1,y2;
  scanf("%f %f %f %f",&x1,&y1,&x2,&y2);
  double xdist=pow((x2-x1),2);
  double ydist=pow((y2-y1),2);
  printf("%.4lf\n",sqrt((xdist+ydist)));
  return 0;
}
