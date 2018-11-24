import java.util.Scanner;

public class Solution {
    static int jumpingOnClouds(int[] cloud_array, int length) {
        int pos = 0;
        int steps = 0;

        while (pos <= length - 1) {
            if (pos+2 < length && cloud_array[pos+2] == 0)
                pos += 2;
            else if (pos+1 < length && cloud_array[pos+1] == 0)
                pos += 1;
            else
                break;
            
            steps += 1;
        }

        return steps;
    }

    public static void main(String[] args) {
        final Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] cloud_array = new int[n];

        String[] cItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int cItem = Integer.parseInt(cItems[i]);
            cloud_array[i] = cItem;
        }

        System.out.println(jumpingOnClouds(cloud_array, n));
        scanner.close();
    }
}

