#include "Board.h"
#include <experimental/random>
#include <algorithm>
#include <iostream>
using namespace std::experimental;
using namespace std;


Board::Board(int rows, int cols) {
    this->n_rows = rows;
    this->n_cols = cols;

    board.assign(rows, vector<int>(cols));
    this->populate_mines();
}


void Board::populate_mines() {
    // Randomly select number of mines
    int n_mines = randint(1, static_cast<int>(this->n_cols * this->n_rows * 0.25));
    cout << "Number of mines: " << n_mines << endl;

    while (n_mines--) {
        // Randomly select a row and column intersection
        int rand_col = randint(1, this->n_cols) - 1;
        int rand_row = randint(1, this->n_rows) - 1;

        this->board[rand_row][rand_col] = 9;

        this->populate_neighbour(rand_row, rand_col);
    }
}


void Board::populate_neighbour(int r, int c) {
    if ((r - 1) >= 0 && this->board[r-1][c] != 9)
        this->board[r-1][c] += 1;

    if ((r + 1) <= (this->n_rows - 1) && this->board[r+1][c] != 9)
        this->board[r+1][c] += 1;

    if ((c + 1) <= (this->n_cols - 1) && this->board[r][c+1] != 9)
        this->board[r][c+1] += 1;

    if ((c - 1) >= 0 && this->board[r][c-1] != 9)
        this->board[r][c-1] += 1;

    if ((r - 1) >= 0 && (c - 1) >= 0 && this->board[r-1][c-1] != 9)
        this->board[r-1][c-1] += 1;

    if ((r + 1) <= (this->n_rows - 1) && (c + 1) <= (this->n_cols - 1) && this->board[r+1][c+1] != 9)
            this->board[r+1][c+1] += 1;

    if ((r - 1) >= 0 && (c + 1) <= (this->n_cols - 1) && this->board[r-1][c+1] != 9)
            this->board[r-1][c+1] += 1;

    if ((r + 1) <= (this->n_rows - 1) && (c - 1) >= 0 && this->board[r+1][c-1] != 9)
            this->board[r+1][c-1] += 1;

}


int Board::rows() {
    return this->n_rows;
}


int Board::columns() {
    return this->n_cols;
}


ostream& operator<<(ostream& stream, Board& obj) {
    for_each(obj.board.begin(), obj.board.end(), [&](vector<int> r) {
        for_each(r.begin(), r.end(), [&](int e) {
            stream << e << " ";
        });
        stream << endl;
    });
    return stream;
}
