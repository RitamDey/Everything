import java.util.Scanner;


class Solution {
    public static void main(String[] args) {
        Scanner ob = new Scanner(System.in);
        
        int test_cases = ob.nextInt(), x_1, y_1, x_2, y_2;
        
        while (test_cases-- != 0) {
            x_1 = ob.nextInt();
            y_1 = ob.nextInt();
            x_2 = ob.nextInt();
            y_2 = ob.nextInt();
            
            // System.out.printf("%d %d %d %d\n", x_1, y_1, x_2, y_2);

            if ((x_1 != x_2) && (y_1 != y_2))
                System.out.println("sad");
            
            else if(x_1 > x_2)
                System.out.println("left");
            else if(x_1 < x_2)
                System.out.println("right");

            else if(y_1 > y_2)
                System.out.println("down");
            else
                System.out.println("up");
        }
    }
}
