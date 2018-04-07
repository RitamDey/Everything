import java.util.Scanner;
import java.util.Stack;


class Solution {
    private static boolean is_balanced(String eq) {
		// Primitive types won't work. So pass the boxed class
        Stack<Character> stack = new Stack<Character>();
        
        for(int i=0; i<eq.length(); ++i) {
            Character curr = eq.charAt(i);
            
            if(curr == '{' || curr == '(' || curr == '[')
                stack.push(curr);
            else {
                if(stack.empty())  // If no opening braces are pushed first
                    return false;
                
                char popped = stack.pop();
                
                if ((curr == '}') && (popped != '{'))
                    return false;
                else if ((curr == ')') && (popped != '('))
                    return false;
                else if ((curr == ']') && (popped != '['))
                    return false;
            }
        }
        
        if(stack.empty())  // Sometimes unclosed braces maybe left
            return true;
        else
            return false;
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (sc.hasNext()) {
            String input=sc.next();
            System.out.println(is_balanced(input));
        }
    }
}

