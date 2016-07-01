#include<stdio.h>

int main()
{
 int s=0,n1,n2,a;
 scanf("%d %d",&n1,&n2);
 if(n1<n2)
 {
  for(a=n1;a<=n2;a++)
  {
   if(a%2)
    s+=a;
   }
  }
  else if(n1>n2)
  {
   for(a=n1;a>=n2;a--)
   {
    if(a%2)
     s+=a;
   }
  }
  printf("%i\n",s);
  return 0;
}
