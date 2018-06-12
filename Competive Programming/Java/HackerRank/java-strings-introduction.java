import java.util.Scanner;


class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		String s1 = sc.nextLine();
		String s2 = sc.nextLine();

		System.out.println(s1.length() + s2.length());

		System.out.println((s1.compareTo(s2) > 0)?"Yes":"No");

		System.out.print(s1.toUpperCase().charAt(0));

		for(int i=1; i<s1.length(); ++i)
			System.out.print(s1.charAt(i));

		System.out.print(" ");

		System.out.print(s2.toUpperCase().charAt(0));

		for(int i=1; i<s2.length(); ++i)
			System.out.print(s2.charAt(i));

		System.out.println();
	}
}

