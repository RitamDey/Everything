#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;


long marcsCakewalk(vector<int> calories, int n) {
    long sum = 0;
    sort(calories.rbegin(), calories.rend());

    for (int i=0; i < n; i++)
        sum += ((unsigned long long)pow(2, i) * calories.at(i));
    

    return sum;
}


int main() {
    int n, tmp;
    cin >> n;

    vector<int> calories;
    for (int i=0; i < n; ++i) {
        cin >> tmp; 
        calories.push_back(tmp);
    }

    cout << marcsCakewalk(calories, n) << endl;
    return 0;
}
