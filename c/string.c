#include<stdio.h>

int main()
{
 int n;
 scanf("%i",&n);
 char s[1000],last;
 fgets(s,1000,stdin);
 last=s[0];
 printf("%c",last);
 for(int a=1;a<n-1;a++)
 {
  if(last!=s[a])
   printf("%c",s[a]);
  last=s[a];
 }
 puts("");
 return 0;
}

