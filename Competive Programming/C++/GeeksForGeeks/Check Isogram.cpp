#include <iostream>
using namespace std;


bool isIsogram(string s);

int main() {
    int t;
    cin >> t;

    while(t--) {
        string s;
        cin >> s;

        cout << isIsogram(s) << endl;
    }

    return 0;
}


bool isIsogram(string s) {
    int *count_table = new int[26];

    for (int pos=0; pos < s.length(); ++pos) {
        count_table[s[pos]]++;

        if (count_table[s[pos]] > 1)
            return 0;
    }

    return 1;
}
