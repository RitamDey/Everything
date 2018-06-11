import java.util.Scanner;


class Google {
  public static String stringSplosion(String str) {
    String res = "";

    for(int pos=0; pos<str.length(); ++pos)
      res += str.substring(0, pos+1);

    return res;
  }

  public static void main(String[] args) {
    System.out.print("Enter a String");

    String input = new Scanner(System.in).nextLine();

    System.out.println(stringSplosion(input));
  }
}
