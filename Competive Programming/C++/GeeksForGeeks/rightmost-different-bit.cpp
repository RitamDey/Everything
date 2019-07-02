#include <iostream>
using namespace std;


int pos(int x, int y) {
    int x_r, y_r, p = 0;

    while ((x > 0) || (y > 0)) {
        x_r = x & 0b1;
        y_r = y & 0b1;
        p += 1;

        if (x_r ^ y_r)
            return p;

        x = x >> 1;
        y = y >> 1;
    }
}


int main() {
    int tests, x, y;

    for(cin >> tests; tests > 0; tests--) {
        cin >> x >> y;
        if ((x ^ y) == 0)
            cout << -1 << endl;
        else
            cout << pos(x, y) << endl;
    }

    return 0;
}
