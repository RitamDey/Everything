#include<iostream>

using namespace std;

class xyz{
  private:
   int  a,b;
 public:
  int add(){
   return a+b;
  }
  void input();
};


void xyz::input(){
  cin>>a>>b;
}

int main(){
  xyz a;
  a.input();
  cout<<a.add();
  return 0;
}
