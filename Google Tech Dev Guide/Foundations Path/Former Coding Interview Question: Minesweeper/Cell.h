#ifndef CELL_H_
#define CELL_H_
#include <ostream>
using namespace std;


class Cell {
    private:
    int count;
    bool bomb;
    bool discovered;

    public:
    Cell(): count(0), bomb(false), discovered(false) {};
    void set_bomb();
    bool is_bomb() {
        return this->bomb;
    }
    void update();
    int get_count() {
        return this->count;
    }
    void discover() {
        this->discovered = true;
    }
    bool is_seen() {
        return this->discovered;
    }
    friend ostream& operator<<(ostream&, Cell&);
};

#endif
