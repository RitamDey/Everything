#include <iostream>
using namespace std;


long search(long *transactions, long length, long target) {
    long low = 0;
    long high = length;
    long curr_target = -1;
    long mid;
    
    while (low < high) {
        mid = (low + high) / 2;
        
        if (transactions[mid] >= target) {
            curr_target = mid + 1;
            high = mid;
        }
        else
            low = mid + 1;
    }
    
    return curr_target;
}


int main() {
    long length, target;
    cin >> length;
    long *transaction = new long[length];
    for (long i=0; i < length; ++i)
        cin >> transaction[i];
    
    long *accumulated = new long[length];
    accumulated[0] = transaction[0];
    
    for (long i=1; i < length; ++i)
        accumulated[i] = accumulated[i-1] + transaction[i];
    
    int cases;
    cin >> cases;
    
    while (cases--) {
        cin >> target;
        cout << search(accumulated, length, target) << endl;
    }
    
    return 0;
}
