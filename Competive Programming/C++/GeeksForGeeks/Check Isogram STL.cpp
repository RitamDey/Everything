#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    string word;
    int cases;

    cin >>  cases;

    while (cases--) {
        cin >> word;
        sort(word.begin(), word.end());

        cout << word << endl;
        // If there are repeating characters, then the iterator will not be at end
        auto pos = adjacent_find(word.begin(), word.end());

        cout << (int) (pos == word.end()) << endl;
    }
    return 0;
}
