import java.util.ArrayList;
import java.util.Scanner;


class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
	ArrayList<ArrayList<Integer>> list = new ArrayList<>();
	ArrayList<Integer> tmpList;

	int length, outIndex, inIndex;

	int cases = sc.nextInt();

	while (cases-- != 0) {
	    length = sc.nextInt();
	    tmpList = new ArrayList<>(length);

	    while (length-- != 0)
	    	tmpList.add(sc.nextInt());
	    
	    list.add(tmpList);
	}

	System.out.println(list);

	cases = sc.nextInt();

	while (cases-- != 0) {
	    outIndex = sc.nextInt();
	    inIndex = sc.nextInt();

	    try {
	    	System.out.println(list.get(outIndex-1).get(inIndex-1));
	    } catch (IndexOutOfBoundsException e) {
	    	System.out.println("ERROR!");
	    }
	}
    }
}
