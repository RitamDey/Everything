import java.util.Scanner;


class Main {
    public static String stringSplosion(String str) {
      String res = "";

      for(int pos=0; pos<str.length(); ++pos) {
        for(int p=0; p<=pos; ++p)
          res += str.charAt(p);
      }
      return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a string: ");
        String input = sc.nextLine();

        System.out.println(stringSplosion(input));
    }
}
