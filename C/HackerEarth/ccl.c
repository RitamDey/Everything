#include<stdio.h>

int main()
{
 int s[30],last;
 int cases;
 scanf("%d",&cases);
 for(int a=1;a<=cases;a++)
 {
  gets(s);
  last=s[0];
  printf("%c",last);
  int pos=1;
  while(s[pos]!="\0")
  {
   if(last!=s[pos])
    printf("%c",s[pos]);
   last=s[pos];
   pos++;
  }
  puts("");
 }
 return 0;
}
