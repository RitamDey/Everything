import java.util.Arrays;
import java.util.Scanner;


class Solution {
    private static int[] sort(int[] array) {
        if (array.length == 0) {
            return array;
        }

        Arrays.sort(array);
        int length = array.length;
        int duplicates = 0;

        for (int i=1; i < length; i++) {
            if (array[i] == array[i-1])
                duplicates++;
        }

        int[] result = new int[length - duplicates];
        int result_index = 1;
        result[0] = array[0];

        for (int i=0; i < length; i++) {
            if (result[result_index-1] != array[i]) {
                result[result_index] = array[i];
                result_index++;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int length = sc.nextInt();
        int[] arr = new int[length];

        for (int i=0; i < length; i++)
            arr[i] = sc.nextInt();

        System.out.println(Arrays.toString(sort(arr)));
    }
}
