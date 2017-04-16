import java.util.Scanner;

class TrimString {
    public static void main(String[] args) {
        String str;
        Scanner sc = new Scanner(System.in);

        while(true) {
            System.out.print("Enter a string to be trimmed ");
            str = sc.nextLine();
            if(str.length() < 1)
                break;
            System.out.println(str.trim());
        }
    }
}
