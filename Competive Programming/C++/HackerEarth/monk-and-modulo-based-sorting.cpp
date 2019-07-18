#include <iostream>
#include <algorithm>
#include <vector>


int main() {
    int len, mod;
    vector<int> array;
    cin >> len >> mod;

    for (int i=0; i < len; i++) {
        int tmp;
        cin >> tmp;
        array.push_back(tmp);
    }

    stable_sort(array.begin(), array.end(), [mod](int i, int j) { return (i%mod) < (j%mod); });
    for_each(array.begin(), array.end(), [](int n) { cout << n << " " });

    return 0;
}
