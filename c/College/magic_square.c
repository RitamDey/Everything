#include <stdio.h>
#include <stdlib.h>

const int size;


void fix_index(int *row, int *col, int *square[size]) {
    // Move up diagonally right
    int proposed_row = *row - 1;
    int proposed_col = *col + 1;
    
    // If we have gone above the first row, then move to the last
    if (proposed_row < 0)
        proposed_row = size - 1;
    
    // If we have gone right towards the last column, then move to the first 
    if (proposed_col >= size)
        proposed_col = 0;
    
    // If we encounter a already filled in cell,
    // insert the new value just in the next row, same column
    if (square[proposed_row][proposed_col] != 0) {
        proposed_row = *row + 1;
        proposed_col = *col;
    }
    
    *col = proposed_col;
    *row = proposed_row;
}


int main() {
    printf("Enter square order: ");
    scanf("%d", &size);
    
    // Static array declaration is not possible with variables
    // So manually allocate them using `calloc()`
    int *square[size];
    for (int r=0; r < size; ++r)
        square[r] = (int *)calloc(size, sizeof(int));
    
    // Calculate the first row and column and insert the first value
    int row = 0;
    int col = size / 2;
    
    square[row][col] = 1;
    
    // Insert rest of the value by first updating the position and then
    // inserting them in the square
    for (int i=2; i <= size * size; ++i) {
        fix_index(&row, &col, square);
        
        square[row][col] = i;
    }
    
    for (int r=0; r < size; ++r) {
        for (int c=0; c < size; ++c)
            printf("%d ", square[r][c]);
        printf("\n");
    }
}
