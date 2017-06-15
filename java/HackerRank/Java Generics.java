class Printer {
    public <Type> void printArray(Type[] arr) {
        for(Type elem: arr)
            System.out.println(elem);
    }
}


class Solution {
    public static void main(String[] args) {
        Printer myPrinter = new Printer();
        
        Integer[] intArray = {1, 2, 3};
        String[] stringArray = {"Hello", "World"};

        myPrinter.printArray(intArray);
        myPrinter.printArray(stringArray);
    }
}
