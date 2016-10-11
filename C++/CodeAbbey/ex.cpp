#include<iostream>
using namespace std;

int main(){
  int range, tmp, sum = 0;
  cin>>range;
  for(int a=0; a<range; ++a){
    cin>>tmp;
    sum += tmp;
  }
  cout<<sum<<endl;
  return 0;
}
