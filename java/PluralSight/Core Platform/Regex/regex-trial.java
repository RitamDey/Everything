import java.util.regex.Pattern;
import java.util.regex.Matcher;


class Regex {
    public static void main(String[] args) {
        String str = "apple apple and cherry please";

        Pattern pattern = Pattern.compile("\\w+");
        Matcher matcher = pattern.matcher(str);

        for(String s: str.split("\\b"))
            System.out.println(s);

        System.out.println();

        while(matcher.find())
            System.out.println(matcher.group());

    }
}