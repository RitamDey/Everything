import java.util.Scanner;
import java.util.Arrays;


class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		String s1 = sc.nextLine().toLowerCase();
		String s2 = sc.nextLine().toLowerCase();

		int[] count1 = new int[26];
		int[] count2 = new int[26];

		boolean anagram = true;

		for(int pos=0; pos<s1.length(); ++pos) {
			count1[((int)s1.charAt(pos))%97] += 1;
		}

		for(int pos=0; pos<s2.length(); ++pos)
			count2[((int)s2.charAt(pos))%97] += 1;

		
		for(int pos=0; pos<26; ++pos) {
			if(count1[pos] != count2[pos]) {
				anagram = false;
				break;
			}
		}

		System.out.println((anagram)?"Anagrams":"Not Anagrams");
	}
}
