import java.util.Scanner;


public class LambdaExample {

    public static void main(String[] args) {
        LambdaExample tester = new LambdaExample();

        // with type declarations
        MathOperation add = (int a, int b) -> a+b;

        // without type declarations
        MathOperation sub = (a, b) -> a-b;

        // with return statment in curly braces
        MathOperation mul = (int a, int b) -> { return a*b; };

        // without return statment and braces
        MathOperation div = (a, b) -> a/b;

        System.out.println("10 + 5 = " + tester.operate(10, 5, add));
        System.out.println("10 - 5 = " + tester.operate(10, 5, sub));
        System.out.println("10 x 5 = " + tester.operate(10, 5, mul));
        System.out.println("10 / 5 = " + tester.operate(10, 5, div));
        
        //with parenthesis
        GreetingService greetService1 = message -> System.out.println("Hello " + message);
        
        //without parenthesis
        GreetingService greetService2 = (message) -> System.out.println("Hello " + message);
        greetService1.sayMessage("sTux");
        greetService2.sayMessage("Joey");
    
    }
        
    interface MathOperation {
        int operation(int a, int b);
    }
    
    interface GreetingService {
        void sayMessage(String message);
    }

    private int operate(int a, int b, MathOperation op) {
        return op.operation(a, b);
    }
}
