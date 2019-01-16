// 
// Decompiled by Procyon v0.5.32
// 

public class Main
{
    public static void main(final String[] array) {
        final int[] array2 = { 229, 102, 166, 229, 227, 205, 80, 224, 122, 168, 56, 185, 1, 154, 43, 127, 139, 83, 211, 202, 240 };
        final int[] array3 = { 212, 7, 249, 175, 162, 155, 49, 191, 62, 247, 90, 214, 108, 248, 116, 62, 255, 60, 190, 163, 155 };
        boolean b = true;
        if (array.length == 0) {
            System.out.println("Usage: ./crackme password");
        }
        else if (array[0].length() != array2.length) {
            System.out.println("Wrong!");
        }
        else {
            for (int i = 0; i < array2.length; ++i) {
                if ((array[0].charAt(i) ^ array2[i]) != array3[i]) {
                    b = false;
                }
            }
            if (b) {
                System.out.println("Success!");
            }
            else {
                System.out.println("Wrong!");
            }
        }
    }
}
