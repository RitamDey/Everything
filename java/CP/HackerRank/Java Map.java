import java.util.Scanner;
import java.util.HashMap;


class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int cases = in.nextInt();
        in.nextLine();

        HashMap<String, Integer> mp = new HashMap<String, Integer>();
        String name = "";
        int phone, i;

        for(i=0; i<cases; ++i) {
            name = in.nextLine();
            phone = in.nextInt();
            in.nextLine();

            mp.put(name, phone);
        }

        while(in.hasNext()) {
            name = in.nextLine();

            if(mp.containsKey(name))
                System.out.println(name+"="+mp.get(name));
            else
                System.out.println("Not found");
        }
    }
}
