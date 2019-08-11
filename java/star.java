import java.util.Scanner;


class Star {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int total_rows = sc.nextInt();

        int first_half = total_rows / 2;
        int second_half = total_rows / 2;

        for (int i=1; i <= first_half; i++) {
            for (int j=1; j <= (first_half - i); j++)  // Decides the spacing before the stars
                System.out.print(" ");
            for (int j=1; j <= i; j++)  // Loop to print the stars
                System.out.print("* ");
            System.out.println("");
        }

        for (int i=second_half; i > 0; i--) {
            for (int j=1; j <= (second_half - i); j++)  // Decides the spqcing before the stars
                System.out.print(" ");
            for (int j=1; j <= i; j++)  // Loop to print the stars
                System.out.print("* ");
            System.out.println("");
        }
    }
}
