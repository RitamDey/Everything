#include <iostream>
#include <string>
using namespace std;

int main() {
    string str_a, str_b;
    cin >> str_a >> str_b;

    cout << str_a.size() << " " << str_b.size() << endl;

    cout << str_a + str_b << endl;

    cout << str_b[0];
    for (int i=1; i < str_a.size(); ++i)
        cout << str_a[i];
    
    cout << " ";
    
    cout << str_a[0];
    for (int i=1; i < str_b.size(); ++i)
        cout << str_b[i];
    
    cout << endl;
    return 0;
}
