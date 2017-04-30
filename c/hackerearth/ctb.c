#include<stdio.h>

int tobin(int n)
{
	int s=0;
	while(n!=0)
	{
		int x=n%2;
		s+=x;
		n/=2;
	}
	return s;
}
int main()
{
  int n;
  scanf("%d",&n);
  printf("%d\n",tobin(n));
}
