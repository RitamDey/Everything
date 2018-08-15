import java.util.Scanner;


class TestClass {
	static int matrix[][];
	static int row, col;


	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);

		row = sc.nextInt();
		col = sc.nextInt();

		matrix = new int[row][col];

		for (int r=0; r < row; ++r) {
			for (int c=0; c < col; ++c)
				matrix[r][c] = sc.nextInt();
		}

		transpose();

		for (int c=0; c < col; ++c) {
			for (int r=0; r < row; ++r)
				System.out.println(matrix[c][r] + " ");
			System.out.println("");
		}
	}

	public static void transpose() {
		int res[][] = new int[col][row];

		for (int r=0; r < row; ++r) {
			for (int c=0; c < col; ++c)
				res[c][r] = matrix[r][c];
		}

		matrix = res;
	}
}
