#include<iostream>
using namespace std;
int main()
{
 int num;
 cin>>num;
 for(int a=1;a<=6;a++)
 {
 if(num%2==0)
  num++;
  cout<<num<<endl;
  num+=2;
 }
 return 0;
}
