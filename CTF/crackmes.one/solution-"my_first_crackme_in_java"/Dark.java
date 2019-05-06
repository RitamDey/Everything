package defpackage;

import java.lang.reflect.Array;
import java.util.ArrayList;

/* renamed from: Dark */
public class Dark {
    int c2;
    int c3;
    int c4;
    char ch1;
    char ch2;
    char ch3;
    int d;
    int n1;
    int n2;
    int n3;
    String permuation4th;
    String permuation11th;
    String permuation18th;
    String s5;
    String s6;
    int y;
    int y1;
    int y2;

    public boolean StrM(String selectedMenuOption, String keyInput, int nameInputSum) {
        ArrayList<String> permut = new PermutationGenerator(selectedMenuOption.substring(0, 5)).getPermutations();
        this.permuation4th = (String) permut.get(3);   // Get the 4th permutation of the string
        this.permuation11th = (String) permut.get(10);  // Get the 11th permuatation of the string
        this.permuation18th = (String) permut.get(17);  // Get the 18th permuatation of the string
        
        // Get the 4th chracter from all the strings
        this.ch1 = this.permuation4th.charAt(3);
        this.ch2 = this.permuation11th.charAt(3);
        this.ch3 = this.permuation18th.charAt(3);
        this.n1 = this.ch1;
        this.n2 = this.ch2;
        this.n3 = this.ch3;
        /**
         * if the value of parameter selectedMenuOption is 'India', then the values of
         * ch1/n1 = a
         * ch2/n2 = n
         * ch3/n3 = d
        **/

        
        // Shift the sum of characters of name rightside by 2 places
        nameInputSum <<= 2;
        
        // Basically asigns the `nameInputSum` to c2
        this.c2 = nameInputSum & 255;
        this.c3 = this.c2 ^ nameInputSum;
        this.c4 = this.c3 | nameInputSum;
        this.d = (((((this.c2 * 2) + (this.c3 * 3)) + (this.c4 * 4)) + (this.n1 * 10)) + (this.n2 * 11)) + (this.n3 * 12);
        /**
         * if the given name is 'Ritam', then the values of the following variables at this point is
         * nameInputSum = 2036 
         * c2           = 244 
         * c3           = 1792
         * c4           = 2036
         * d            = 17388
        **/
        this.s5 = String.valueOf(this.d);
        this.s6 = this.s5;
        this.s5 = this.s5.substring(0, 2);
        this.y = Integer.parseInt(this.s5);
        this.y1 = Integer.parseInt(this.s6);
        /**
         * At this point, the value of
         * y  = 173
         * y1 = 17388
        **/
        a = new int[3][];
        a[0] = new int[]{2, 2, this.y};
        a[1] = new int[]{4, 6, 2};
        a[2] = new int[]{3, 4, 4};  // a = {{2, 2, 173}, {4, 6, 2}, {3, 4, 4}}

        int[][] b = new int[][]{new int[]{2, 2, 3}, new int[]{8, 9, 5}, new int[]{6, 2, 2}};  // b = {{2, 2, 3}, {8, 9, 5}, {6, 2, 2}}
        int[][] c = (int[][]) Array.newInstance(Integer.TYPE, new int[]{3, 3});  // c = {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}}
        
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                c[i][j] = 0;
                for (int k = 0; k < 3; k++) {
                    c[i][j] = c[i][j] + (a[i][k] * b[k][j]);
                }
            }
        }
        this.y2 = c[2][2];
        this.y2 *= this.y1;
        if (keyInput.equals(String.valueOf(this.y2))) {
            return true;
        }
        return false;
    }
}
