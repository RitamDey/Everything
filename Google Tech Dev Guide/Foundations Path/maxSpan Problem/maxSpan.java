import java.util.Scanner;


class Main {
  public static int leftmost(int[] nums, int elem) {
    for(int pos=nums.length-1; pos >= 0; --pos) {
      if(nums[pos] == elem)
        return pos;
    }
    return -1;
  }


  public static int maxSpan(int[] nums) {
    int span = 0, temp;

    for(int pos=0; pos < nums.length; ++pos) {
      int last_pos = leftmost(nums, nums[pos]);
      if(last_pos != -1){
        temp = Math.abs(pos - last_pos) + 1;
        span = (temp > span)? temp:span;
      }
    }

    return span;
  }

  public static void main(String[] args) {
    int[] arr1 = {1, 2, 1, 1, 3};
    int[] arr2 = {1, 4, 2, 1, 4, 1, 4};
    int[] arr3 = {1, 4, 2, 1, 4, 4, 4};

    System.out.println(maxSpan(arr1));
    System.out.println(maxSpan(arr2));
    System.out.println(maxSpan(arr3));
  }
}
