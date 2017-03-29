#include <iostream>
using namespace std;


template <class T>
T div(T num1, T num2) {
    return num1/num2;
}

int main(){
    printf("%d\n", div(5,5));
    printf("%f\n", div(4.0,8.0));
    return 0;
}
