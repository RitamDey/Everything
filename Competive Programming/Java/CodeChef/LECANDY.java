import java.util.Scanner;


class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int cases = sc.nextInt();

        while (cases-- != 0) {
            int n_elephants = sc.nextInt();
            long n_candies = sc.nextInt();

            long sum = 0;

            while (n_elephants-- != 0)
                sum += sc.nextInt();

            if (sum <= n_candies)
                System.out.println("Yes");
            else
                System.out.println("No");
        }
    }
}
