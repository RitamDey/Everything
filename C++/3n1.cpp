#include<iostream>
using namespace std;
int main()
{
 int n;
 cin>>n;
 while(true)
 {
  cout<<n<<" ";
  if(n==1)
   break;
  else if(n%2)
   n=3*n+1;
  else
   n/=2;
  }
 cout<<endl;
 return 0;
}
