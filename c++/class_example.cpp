#include <iostream>
using namespace std;

class MyClass {
    public:
    MyClass(int a, int b) {
        regVar = a; //Regular variable initializer
        :constVar(b)
    void print();

    private:
    int regVar;
    const int constVar;
}

MyClass::void print() {
    cout<<regVar<<constVar<<endl;
}

int main() {
    MyClass obj(5, 6);
    return 0;
}