#include<stdio.h>

int palindrome(int n)
{
 int rev=0;
 while(n)
 {
  int x=n%10;
  rev=rev*10+x;
  n/=10;
 }
if(rev==n)
 return 1;
}
