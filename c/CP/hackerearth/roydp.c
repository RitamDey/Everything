#include<stdio.h>

int main()
{
  int l,n,h,w;
  scanf("%d",&l);
  scanf("%d",&n);
  for(int a=1;a<=n&&scanf("%d %d",&h,&w);a++)
  {
    if((h<l)||(w<l))
     puts("UPLOAD ANOTHER");
    else
    {
      if(h==w)
       puts("ACCEPTED");
      else
       puts("CROP IT");
    }
  }
  return 0;
}
