import java.util.Scanner;


class Solution {
    static int simpleArraySum(int[] arr) {
        int sum = 0;

        for (int n: arr)
            sum += n;

        return sum;
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int arrCount = sc.nextInt();

        int[] arr = new int[arrCount];

        for (int arrItr = 0; arrItr < arrCount; arrItr++)
            arr[arrItr] = scanner.nextInt();

        System.out.println(simpleArraySum(arr));
    }
}
