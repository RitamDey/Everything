import java.text.MessageFormat;


class Format {
    public static void main(String[] args) {
        System.out.println(MessageFormat.format("{0} {1} {0}", "a", "b", "c"));
        System.out.println(MessageFormat.format("{0} {1} {0}", "a"));
    }
}
