#include <iostream>
using namespace std;


template <class T>
T div(T num1, T num2) {
    return num1/num2;
}

int main(){
    cout << div(5, 5) << endl;
    cout << div(4,8)  << endl;
}
