#include <stdio.h>


int main() {
	int row_1, col_1, row_2, col_2;

	printf("Enter rows and column dimensions for matrix 1: ");
	scanf("%d %d", &row_1, &col_1);

	printf("Enter rows and column dimensions for matrix 2: ");
	scanf("%d %d", &row_2, &col_2);

	int matrix_1[row_1][col_1];
	int matrix_2[row_2][col_2];

	if ((row_1 != row_2) || (col_1 != col_2)) {
	    fprintf(stderr, "ERROR: Dimension mismatch\n");
	    return -1;
	}

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

	int res[row_2][col_2];

	for (int r=0; r < row_1; ++r) {
	    for (int c=0; c < col_1; ++c) {
                res[r][c] = matrix_1[r][c] + matrix_2[r][c];
	    }
	}

	for (int r=0; r < row_1; ++r) {
	    for (int c=0; c < col_1; ++c)
	        printf("%d ", res[r][c]);
	    printf("\n");
	}

	return 0;
}
