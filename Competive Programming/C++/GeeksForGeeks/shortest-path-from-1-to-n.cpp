#include <iostream>
using namespace std;


inline bool is_divisible(int n) {
    return (n % 3) == 0;
}


int shortest_path(int j) {
    int curr_vertex = j;
    int path_length = 0;

    while (curr_vertex > 1) {
        if (is_divisible(curr_vertex))
            curr_vertex /= 3;
        else
            curr_vertex -= 1;

        path_length += 1;
    }

    return path_length;
}


int main() {
    int cases;
    int n;

    cin >> cases;

    while (cases--) {
        cin >> n;
        cout << shortest_path(n) << endl;
    }

    return 0;
}
