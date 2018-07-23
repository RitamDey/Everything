import java.util.Scanner;
import java.util.HashMap;


class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
	HashMap<String, Integer> map = new HashMap<>();

	int length = sc.nextInt();
	int message = sc.nextInt();

	sc.nextLine();

	for (String key: sc.nextLine().split(" ")) {
	    int count = map.getOrDefault(key, 0) + 1;
	    map.put(key, count);
	}

	boolean possible = true;
	int count;

	for (String key: sc.nextLine().split(" ")) {
	    if ((count = map.getOrDefault(key, 0)) > 0)
		map.put(key, count - 1);
	    else {
	    	possible = false;
	    	break;
	    }
	}

	System.out.println((possible) ? "Yes" : "No");
    }
}
