#include <iostream>
using namespace std;


bool isKth(int n, int k) {
    return (n & (0b1 << k)) != 0;
}


int main() {
    int n, k, tests;

    for (cin >> tests; tests > 0; tests--) {
        cin >> n >> k;

        cout << (isKth(n, k) ? "Yes": "No") << endl;
    }

    return 0;
}
