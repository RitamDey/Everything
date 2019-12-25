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
}
