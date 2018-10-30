import java.util.Scanner;


class Solution {
    public static int power(int n) {
        if (n == 0)
            return 1;

        int res = power(n/2);

        if (n%2 == 0)
            return res * res;
        else
            return res * res * 3;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        System.out.println(power(n));
    }
}
