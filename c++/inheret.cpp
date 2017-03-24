#include <iostream>
using namespace std;

class Rectangle{
    private:
        int lenght, breadth;
public:
  void init(int len, int breadth){
    lenght = len;
    breadth  = breadth;
  }

  int area(){
    return lenght*breadth;
  }
}

  class Square:Rectangle{
  public:
    void init(int len){
      lenght = breadth = len;
    }
  }

    int main(){
      Rectangle rt;
      Square sq;
      int len, 
