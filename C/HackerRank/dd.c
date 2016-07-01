#include<stdio.h>
#include<stdlib.h>
int main()
{
 int size;
 scanf("%i",&size);
 int matrix[size][size];
 for(int a=0;a<size;a++)
 {
  for(int b=0;b<size;b++)
   scanf("%d",&matrix[a][b]);
 }
 int pos=0;
 int s=0;
 for(int a=0;a<size;a++)
 {
  s+=matrix[a][pos];
  pos++;
 }
 int s1=0;
 pos=size-1;
 for(int a=0;a<size;a++)
 {
  s1+=matrix[a][pos];
  pos--;
 }
 s1=abs(s-s1);
 printf("%i\n",s1);
 return 0;
}
