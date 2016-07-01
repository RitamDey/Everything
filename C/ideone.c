#include<stdio.h>

int main()
{
  for(int a=0,max;scanf("%d",&max),a<=max;a++)
  {
    char s[200];
    gets(s);
    //scanf("%200s",s);
    //char *sp=s;
    int size=sizeof(s)-1;
    //while(*s!="\0")
    while(s[a]!="\0")
    {
      for(int a=0;a<=size/2;a++)//,s++)
      {
        if(a%2==0)
        {
          printf("%s",s);
        }
        //s++;
      }
    }
  }
  return 0;
}
