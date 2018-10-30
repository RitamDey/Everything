import java.util.Scanner;


class Solution {
    public static int power(int base, int n) {
        if (n == 0)
            return 1;

        int res = power(base, n/2);

        if (n%2 == 0)
            return res * res;
        else
            return res * res * base;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter base and power: ");
        int base = sc.nextInt();
        int pow = sc.nextInt();

        System.out.println(power(base, pow));
    }
}
