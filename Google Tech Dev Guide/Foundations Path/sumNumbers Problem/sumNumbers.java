import java.util.Scanner;


class Solution {
  public static int sumNumbers(String str) {
    String temp = "";
    int length = str.length();
    int sum = 0;
    char tmp;


    for(int pos=0; pos<length; ++pos) {
      tmp = str.charAt(pos);
      if(Character.isDigit(tmp))
        temp += tmp;
      else {
        if(temp != "") {
          sum += Integer.parseInt(temp);
          temp = "";
        }
      }
    }

    if(temp != "")
      sum += Integer.parseInt(temp);

    return sum;
  }

  public static void main(String[] args) {
    String str = new Scanner(System.in).nextLine();

    System.out.println(sumNumbers(str));
  }
}
