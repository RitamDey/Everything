#include<stdio.h>
int main()
{
  int n;
  scanf("%i",&n);
  for(int a=1;a<=n;a++)
  {
    for(int b=1;b<=a;b++)
    {
      //for(int c=1;c<n;c++,printf(" "));
      printf("#");
    }
    printf("\n");
  }
}
