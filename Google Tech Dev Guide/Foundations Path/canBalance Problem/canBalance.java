class Solution {
  public static boolean canBalance(int[] nums) {
    int sum = 0;
    int left=0, right;
    for(int i: nums)
      sum += i;

    for(int i: nums) {
      left += i;
      right = sum - left;

      if(left == right)
        return true;
    }
    return false;
  }

  public static void main(String[] args) {
    int[] arr1 = {1, 1, 1, 2, 1};
    int[] arr2 = {2, 1, 1, 2, 1};
    int[] arr3 = {10, 10};

    System.out.println(canBalance(arr1));
    System.out.println(canBalance(arr2));
    System.out.println(canBalance(arr3));
  }
}
