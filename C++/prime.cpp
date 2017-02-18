#include<iostream>
#include<math.h>
using namespace std;
int main()
{
  int n,a;
  cin>>n;
  int n2=sqrt(n);
  cout<<n;
  for(a=2;a<=n2;a++)
  {
    if(n%a==0)
      cout<<" is composite"<<endl;
  }
  if((a-1)==n2)
   cout<<" is Prime"<<endl;
  return 0;
}
