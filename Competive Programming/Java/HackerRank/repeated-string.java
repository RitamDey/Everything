import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

class Solution {

    // Complete the repeatedString function below.
    static long repeatedString(String s, long n) {
        long count_a = 0;
        long times = n / s.length();
        long rem = n % s.length();

        for (int pos=0; pos < s.length(); ++pos) {
            if (s.charAt(pos) == 'a')
                count_a++;
        }

        count_a *= times;

        for (int pos=0; pos < rem; ++pos) {
            if (s.charAt(pos) == 'a')
                count_a++;
        }

        return count_a;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = scanner.nextLine();

        long n = scanner.nextLong();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        long result = repeatedString(s, n);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}

