#include<stdio.h>

int main()
{
  int cases;
  char s[30],l;
  scanf("%d",&cases);
  for(int a=1;a<=cases;a++)
  {
    //fgets(s,30,stdin);
    scanf("%30s",&s);
    for(int b=0;b<30;b++)
    {
      printf("%s",s[b]);
      if(s[b+1]==s[b])
       b++;
    }
    printf("\n");
   }
 }
