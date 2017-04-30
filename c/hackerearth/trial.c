#include<stdio.h>
#include<string.h>
//#include<ctype.h>
int main()
{
 char s[]="abcdE";
 for(int a=0;a<=strlen(s);a++)
 {
  if((s[a]>='a')&&(s[a]<='z'))
   printf("%s",toupper(s[a]));
  else
   printf("%s",tolower(s[a]));
 }
}
