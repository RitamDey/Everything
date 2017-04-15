import java.math.BigInteger;
import java.util.Scanner;


class Solution {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        BigInteger num1 = BigInteger.valueOf(scan.nextLong());
        BigInteger num2 = BigInteger.valueOf(scan.nextLong());

        System.out.println(num1.add(num2));
        System.out.println(num1.multiply(num2));
    }
}