#include<iostream>

using namespace std;

int pow(double a, int n) {
    if(n==0)
        return 1;
    else if(n==1)
        return a;
    double t = pow(a, n/2);
    return t * t * pow(a, n%2);
}

int main(){
    double a, b;
    cout<<"Enter two numbers: ";
    cin>>a>>b;
    cout<<a<<" raised to the power of "<<b<<" is "<<pow(a,b)<<endl;
    return 0;
}
