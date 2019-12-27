#include "Board.h"
#include <iostream>
using namespace std;


int main() {
    int rows;
    cout << "Number of row: ";
    cin >> rows;
    int cols;
    cout << "Number of columns: ";
    cin >> cols;

    Board obj(rows, cols);

    cout << obj;

    /**if (obj.at(3, 1) == -2)
        cout << "Discovered the bomb" << endl;
**/
    cout << "Discovered " << obj.at(0, 0) << " number of cells" << endl;
    cout << obj;
}
