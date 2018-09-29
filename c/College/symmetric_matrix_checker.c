#include <stdio.h>


int main() {
    int row, col;
    
    printf("Enter matrix dimensions (rows and columns): ");
    scanf("%d %d", &row, &col);
    
    int matrix[row][col];
    
    for (int r=0; r < row; ++r) {
        for (int c=0; c < col; ++c) {
            printf("Matrix [%d][%d]: ", r+1, c+1);
            scanf("%d", &matrix[r][c]);
        }
    }

    if (row != col) {
        puts("Not symmetric");
        return 0;
    }
    
    int res[col][row];
    
    for (int r=0; r < row; r++) {
        for (int c=0; c < col; c++)
            res[c][r] = matrix[r][c];
    }
    
    for (int r=0; r < col; ++r) {
        for (int c=0; c < row; ++c) {
            if (res[r][c] != matrix[r][c]) {
                puts("Not Symmetric");
                return 0;
            }
        }
    }

    puts("Symmetric");
    
    return 0;
}
