class ForEach {
	public static void main(String[] args) {
		int[] nums1 = {1, 2, 3, 4, 5};
		int sum = 0;

		for(int x: nums1)
			sum += x;

		System.out.println("Summation is " + sum);

		int[][] nums = new int[3][5];

		for(int i=0; i < 3; ++i)
			for(int j=0; j<5; ++j)
				nums[i][j] = (i+1)*(j+1);

		// Iterating over multi-dimensional array needs a array type
		for(int[] x: nums) {
			// Normal iterator to iterate over a simple array
			for(int y: x) {
				System.out.println("Value is " + y);
				sum += y;
			}
		}

		System.out.println("Summation is " + sum);
	}
}
