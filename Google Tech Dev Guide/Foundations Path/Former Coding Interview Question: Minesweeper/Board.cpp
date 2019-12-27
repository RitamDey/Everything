#include <experimental/random>
#include <algorithm>
#include <set>
#include <utility>
#include "Board.h"
using namespace std::experimental;
using namespace std;


class Queue {
    private:
    set<pair<int, int>> cell_queue;

    public:
    void enqueue(pair<int, int> cell) {
        this->cell_queue.insert(cell);
    }

    pair<int, int> dequeue() {
        set<pair<int, int>>::iterator begin = this->cell_queue.begin();
        pair<int, int> cell = *begin;

        this->cell_queue.erase(begin);

        return cell;
    }

    bool is_empty() {
        return this->cell_queue.empty();
    }
};


Board::Board(int rows, int cols) {
    this->n_rows = rows;
    this->n_cols = cols;

    board.assign(rows, vector<Cell>(cols));
    this->populate_mines();
}


void Board::populate_mines() {
    // Randomly select number of mines
    int n_mines = randint(1, static_cast<int>(this->n_cols * this->n_rows * 0.1));
    cout << "Number of mines: " << n_mines << endl;

    while (n_mines--) {
        // Randomly select a row and column intersection
        int rand_col = randint(1, this->n_cols) - 1;
        int rand_row = randint(1, this->n_rows) - 1;

        this->board[rand_row][rand_col].set_bomb();

        this->populate_neighbour(rand_row, rand_col);
    }
}


vector<pair<int, int>> Board::neighbours(pair<int, int> cell) {
    auto [r, c] = cell;
    vector<pair<int, int>> result;

    if ((r - 1) >= 0)
        result.push_back(make_pair(r - 1, c));

    if ((r + 1) <= (this->n_rows - 1))
        result.push_back(make_pair(r + 1, c));
    
    if ((c - 1) >= 0)
        result.push_back(make_pair(r, c - 1));

    if ((c + 1) <= (this->n_cols - 1))
        result.push_back(make_pair(r, c + 1));

    if ((r - 1) >= 0 && (c - 1) >= 0)
        result.push_back(make_pair(r - 1, c - 1));

    if ((r - 1) >= 0 && (c + 1) <= (this->n_cols - 1))
        result.push_back(make_pair(r - 1, c + 1));

    if ((r + 1) <= (this->n_rows - 1) && (c - 1) >= 0)
        result.push_back(make_pair(r + 1, c - 1));

    if ((r + 1) <= (this->n_rows - 1) && (c + 1) <= (this->n_cols - 1))
        result.push_back(make_pair(r + 1, c + 1));

    return result;
}


void Board::populate_neighbour(int r, int c) {
    vector<pair<int, int>> valid_neighbours = this->neighbours(make_pair(r, c));

    for_each(valid_neighbours.begin(), valid_neighbours.end(), [this](pair<int, int> cell_pos) {
        auto[r, c] = cell_pos;
        Cell& cell = this->board[r][c];
        cell.update();
    });
}


int Board::rows() {
    return this->n_rows;
}


int Board::columns() {
    return this->n_cols;
}


ostream& operator<<(ostream& stream, Board& obj) {
    stream << "*|";
    for (int i=1; i <= obj.n_cols; i++)
        stream << i << " ";
    stream << endl;
    for (int i=1; i <= obj.n_cols+1; i++)
        stream << "= ";
    stream << endl;

    int i = 1;

    for_each(obj.board.begin(), obj.board.end(), [&](vector<Cell> r) {
        stream << i++ << "|";
        for_each(r.begin(), r.end(), [&](Cell e) {
            stream << e << " ";
        });
        stream << endl;
    });
    return stream;
}


int Board::at(int row, int col) {
    /**
     * Set the user specified cell as discovered and start disovering other safe cells
     * Returns the number of cell discovered.
     * -1 if the arguments are out of bounds
     * -2 if the arguments points to a bomb
    **/
    int cell_count = 0;
    if ((row > this->n_rows - 1) || (col > this->n_cols - 1) || (row < 0) || (col < 0))
        return -1;

    Queue q;
    q.enqueue(make_pair(row, col));
    Cell& cell = this->board[row][col];

    if (cell.is_bomb()) {
        // User Clicked on a bomb. Terminate the game
        cell.discover();
        return -2;
    } else if (cell.is_seen()) {
        // User clicked on an already discovered cell. Do noting.
        return 0;
    }

    while (!q.is_empty()) {
        // Unpack the cell co-ordinates and mark it as discovered
        auto [row, col] = q.dequeue();
        this->board[row][col].discover();
        cell = this->board[row][col];
        cell_count++;

        if (cell.get_count() > 0)
            // No need to discover neighbours of cells whose counts are > 0, i.e non-zero
            continue;

        for (auto n: this->neighbours(make_pair(row, col))) {
            cell = this->board[n.first][n.second];
            if (!cell.is_seen() && !cell.is_bomb()) {
                q.enqueue(n);
            }
        }
    }

    return cell_count;
}
