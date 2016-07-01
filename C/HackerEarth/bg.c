#include<stdio.h>
int findgirl(char *);
int main()
{
  int n,s;
  scanf("%d",&n);
  for(int a=1;a<=n&&scanf("%d",&s);a++)
  {
    char stud[s*2+1];
    scanf("%s",s);
    for(int b=0;stud[b]!='\0';s++)
    {
      if(stud[b]=='B')
       if(stud[b+1]=='B')
       {
         int pos=findgirl(stud[b]);
         char g=stud[pos];
         stud[pos]=stud[b];
         stud[b]=stud[pos];
       }
    }
  }
  return 0;
}
int findgirl(char *c)
{
  int p=0;
  while(*c!='G')
   p++;
  return p;
}
