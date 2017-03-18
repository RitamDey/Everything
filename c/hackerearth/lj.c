#include <stdio.h>
int main()
{
  unsigned long int n;
  int s=0;
  scanf("%lu",&n);
  printf("%lu",n);
  while(n!=0)
  {
    int x=n%10;
    n/=10;
    const int k=x;
    x=n%10;
    n/=10;
    if(x==k)
     s++;
  }
  if(s==6)
   printf("Sorry ,Sorry\n");
}
