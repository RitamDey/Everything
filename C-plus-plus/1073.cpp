#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
  int num;
  cin>>num;
  for(int a=2;a<=num;a+=2)
   cout<<a<<"^"<<a<<pow(a,2);
  return 0;
}
