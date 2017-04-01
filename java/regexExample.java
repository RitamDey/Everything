import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexExample {
    public static void main(String[] args) {
	String line = "This order was placed for QT3000! OK?";
	String regex = "(.*)(\\d+)(.*)";

	// Create a Pattern Object
	Pattern pattern = Pattern.compile(regex);

	// Create a Matcher Object
	Matcher match = pattern.matcher(line);

	if(match.find()){
	    System.out.println("Found value: "+match.group(0)+"\nFound value: "+match.group(1)+"\nFound value: "+match.group(2));
	}
	else{
	    System.out.println("Not found!!!!");
	}
    }
}
