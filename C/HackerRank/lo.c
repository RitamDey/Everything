#include <stdio.h>

int main()
{
	int size,count=-1,term;
	scanf("%d %d",&size,&term);
	int arr[size];
	for(int a=0;a<size;a++)
	 scanf("%d",&arr[a]);
	for(int a=size-1;a>0;a--)
	{
		if(arr[a]==term)
		{
		 printf("%i",a+1);
		 count=0;
		}
	}
	if(count==-1)
	 printf("%i",count);
    return 0;

}
