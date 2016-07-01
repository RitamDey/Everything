#include<iostream>
using namespace std;
int main()
{
 int n=100;
 unsigned long int f=1;
 for(int a=1;a<=n;a++)
  f*=a;
 cout<<f<<endl;
 unsigned long int s=0;
 while(f)
 {
  s+=(f%10);
  f/=10;
 }
 cout<<s<<endl;
 return 0;
}
