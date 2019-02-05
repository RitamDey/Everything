import java.util.Arrays;
import java.util.Scanner;


public class Solution {
    static int minimumAbsoluteDifference(int[] arr, int length) {
        Arrays.sort(arr);

        int minimumDifference = Math.abs(arr[0] - arr[1]);

        for (int i=0; i < length - 1; ++i) {
            int diff = Math.abs(arr[i] - arr[i+1]);
            if (diff < minimumDifference)
                minimumDifference = diff;
        }

        return minimumDifference;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int length = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        int[] arr = new int[length];
        for (int i = 0; i < length; i++) {
            arr[i] = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        }

        System.out.println(minimumAbsoluteDifference(arr, length));
        scanner.close();
    }
}

