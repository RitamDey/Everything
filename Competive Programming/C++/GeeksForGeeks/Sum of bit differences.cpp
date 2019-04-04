using namespace std;

inline int discardLeft(int n) {
    return n >> 1;
}


inline int getLastBit(int n) {
    return n & 1;
}

int countDiffer(int n, int n2) {
    int count = 0, last_bit_n, last_bit_n2;
    
    while ((n | n2) != 0) {
        if (getLastBit(n) != getLastBit(n2))
            count += 1;
        
        n = discardLeft(n);
        n2 = discardLeft(n2);
    }
    
    return count;
}


int main() {
    int cases, len, count;
    int *arr;
    cin >> cases;
    
    while (cases--) {
        cin >> len;
        count = 0;
        
        arr = new int[len];
        
        for (int i=0; i < len; ++i)
            cin >> arr[i];
            
        for (int i=0; i < len; ++i) {
            for (int j=0; j < len; ++j)
                count += countDiffer(arr[i], arr[j]);
        }
        
        cout << count << endl;
    }
    
	return 0;
}
