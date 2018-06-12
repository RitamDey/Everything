import java.util.Scanner;
import java.util.Arrays;


class Solution {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);

		String s = in.nextLine();
		int start = in.nextInt();
		int end = in.nextInt();

		char[] res = new char[end - start];
		s.getChars(start, end, res, 0);

		for(char c: res)
			System.out.print(c);

		System.out.println();
	}
}
