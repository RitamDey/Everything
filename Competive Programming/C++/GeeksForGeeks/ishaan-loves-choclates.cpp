#include <iostream>
using namespace std;


int least_tasty(int *choclates, int len) {
    int least = choclates[0];

    for (int i=1; i < len; ++i) {
        if (choclates[i] < least)
            least = choclates[i];
    }

    return least;
}


int main() {
    int cases, *arr, length;
    cin >> cases;

    while (cases--) {
        cin >> length;
        arr = new int[length];

        for (int i=0; i < length; ++i)
            cin >> arr[i];

        cout << least_tasty(arr, length) << endl;
    }

    return 0;
}
