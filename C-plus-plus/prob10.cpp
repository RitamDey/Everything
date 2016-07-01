#include<iostream>
using namespace std;
int prime(int);
int main()
{
 int s=0;
 for(int a=1;a<2000000;a++)
  s+=prime(a);
 cout<<s<<endl;
 return 0;
}

int prime(int n)
{
 int s=0;
 for(int a=1;a<=n;a++)
 {
  if(n%a==0)
   s++;
 }
 if(s==2)
 return n;
 else
 return 0;
}
