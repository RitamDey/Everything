import java.util.Scanner;


class GFG {
	private static boolean divisbilty_fsm(String num) {
		String curr_state = "s0";
		char curr_bit;

		for(int pos=0; pos < num.length(); pos++) {
			curr_bit = num.charAt(pos);
			switch(curr_state) {
				case "s0":
					curr_state = (curr_bit == '0')? "s0": "s1";
					break;
				case "s1":
					curr_state = (curr_bit == '0')? "s2": "s0";
					break;
				case "s2":
					curr_state = (curr_bit == '0')? "s1": "s2";
					break;
				}
			}

			return curr_state == "s0";
		}


	public static void main(String[] args) {
	    int tests;
	    String bitstring;
	    Scanner sc = new Scanner(System.in);


	    for (tests = sc.nextInt(); tests > 0; tests--) {
	        bitstring = sc.nextLine();

	        System.out.println(bitstring);
	        System.out.println(divisbilty_fsm(bitstring));
        }
        
        sc.close();
	}
}
