#include<stdio.h>

int main()
{
 int size;
 scanf("%i",&size);
 int arr[size][size];
 for(int a=0;a<size;a++)
 {
  for(int b=0;b<size;b++)
   scanf("%d",&arr[a][b]);
 }
 for(int a=0;a<size;a++)
  for(int b=0;b<size;b++)
  {
   printf("%i\n",arr[a][b]);
  }
 return 0;
}
