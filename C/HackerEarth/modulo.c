#include<stdio.h>
#include <math.h>
#define modulo (pow(10,9)+7)
int main()
{
  int n;
  scanf("%d",&n);
  int nums,s=1;
  for(int a=0;a<n&&scanf("%d",&nums);a++)
  {
    s=(s*nums)%(int)modulo;
  }
  printf("%d\n",s);
  return 0;
}
