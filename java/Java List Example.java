import java.util.*;
import java.util.Scanner;


class Example {
    public static void main(String[] args) {
        String m = "Hello World!";
        String[] msg = m.split(" ");

        ArrayList arr = new ArrayList<>(Arrays.asList(msg));
        System.out.println(arr);
    }
}
