import java.util.Scanner;


class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String str = sc.nextLine();
		int len = str.length() - 1;

		String rev = "";

		for(; len>=0; --len)
			rev += str.charAt(len);

		System.out.println((str.equals(rev))?"Yes":"No");
	}
}
