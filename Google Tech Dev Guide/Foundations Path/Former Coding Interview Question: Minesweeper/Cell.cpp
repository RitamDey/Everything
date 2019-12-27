#include "Cell.h"


void Cell::set_bomb() {
    this->bomb = true;
    this->count = 9;
}


void Cell::update() {
    if (!bomb)
        this->count++;
}


ostream& operator<<(ostream& stream, Cell& cell) {
    if (cell.discovered) {
        stream << cell.count;
    } else {
        stream << "-";
    }

    return stream;
}
