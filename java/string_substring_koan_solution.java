class SubString {
    public static void main(String[] args) {
        String str = "I AM a number ONE!";
        System.out.println(str.substring(0));
        System.out.println(str.substring(1));
        System.out.println(str.substring(5));
        System.out.println(str.substring(14, 17));
        System.out.println(str.substring(7, str.length()));
    }
}
