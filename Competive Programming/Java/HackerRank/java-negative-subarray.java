import java.util.Scanner;
import java.util.Arrays;


class Solution {
    public static int sum(int[] arr) {
    	int sum = 0;

	for (int n: arr)
	    sum += n;
	
	return sum;
    }

    public static void generate_arrays(int[] arr, int length) {
    	int count = 0;
    	int last_index = 1;

	while(last_index <= length + 1) {
	    for (int pos=0; pos <= (length - last_index); ++pos) {
		int[] slice = Arrays.copyOfRange(arr, pos, pos + last_index);

		if (sum(slice) < 0)
		    count++;
	    }
	    last_index++;
	}

	System.out.println(count);
    }

    public static void main(String[] args) {
    	Scanner sc = new Scanner(System.in);

	int length = sc.nextInt();
	int[] arr = new int[length];

	for (int pos=0; pos < length; ++pos)
	    arr[pos] = sc.nextInt();
	
	generate_arrays(arr, length);
    }
}
