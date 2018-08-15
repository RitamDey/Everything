#include <stdio.h>


void multiply(int row_1, int col_1, int matrix_1[row_1][col_1], int row_2, int col_2,  int matrix_2[row_2][col_2],int res[row_1][col_2]) {
    int r = 0;
    int sum, c;
    
    while (r < row_1) {
        c = 0;
        
        while (c < col_2) {
            sum = 0;
            for (int r_inner=0; r_inner < row_2; ++r_inner)
                sum += matrix_1[r][r_inner] * matrix_2[r_inner][c];
            
            res[r][c] = sum;
            c++;
        }
        
        r++;
    }
}


int main() {
    int row_1, col_1, row_2, col_2;
    
    printf("Enter dimensions of matrix 1: ");
    scanf("%d %d", &row_1, &col_1);
    
    printf("Enter dimensions of matrix 2: ");
    scanf("%d %d", &row_2, &col_2);
    
    if (col_1 != row_2) {
        fprintf(stderr, "ERROR: dimensions mismatch\n");
        return -1;
    }
    
    int matrix_1[row_1][col_1];
    int matrix_2[row_2][col_2];
    
    for (int r=0; r < row_1; ++r) {
        for (int c=0; c < col_1; ++c) {
            printf("Matrix 1 [%d][%d]: ", r+1, c+1);
            scanf("%d", &matrix_1[r][c]);
        }
    }
    
    for (int r=0; r < row_2; ++r) {
        for (int c=0; c < col_2; ++c) {
            printf("Matrix 2 [%d][%d]: ", r+1, c+1);
            scanf("%d", &matrix_2[r][c]);
        }
    }
    
    
    int res[row_1][col_2];
    
    multiply(row_1, col_1, matrix_1, row_2, col_2, matrix_2, res);
    
    for (int r=0; r < row_1; ++r) {
        for (int c=0; c < col_2; ++c)
            printf("%d ", res[r][c]);
        printf("\n");
    }
    
    return 0;
}
