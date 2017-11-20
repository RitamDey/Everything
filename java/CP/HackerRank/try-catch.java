import java.util.Scanner;


class TryCatch {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n1, n2;
        
        try {
            n1 = sc.nextInt();
            n2 = sc.nextInt();

            System.out.println(n1/n2);
        } catch(Exception e) {
            System.out.println(e);
        }
    }
}
