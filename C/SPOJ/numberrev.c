#include<stdio.h>

int main() {
  int n,r=0;
  printf("Enter ");
  scanf("%d",&n);
  while(n!=0)
  {
    int x=n%10;
    r=r*10+x;
    n/=10;
  }
  printf("%d\n",r);
  return 0;
}
