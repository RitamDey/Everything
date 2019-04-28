import java.util.ArrayList;
import java.util.Iterator;

/* renamed from: PermutationGenerator */
class PermutationGenerator {
    private String word;

    public PermutationGenerator(String aWord) {
        this.word = aWord;
    }

    public ArrayList<String> getPermutations() {
        ArrayList<String> result = new ArrayList<>();
        if (this.word.length() == 0) {
            result.add(this.word);
        } else {
            for (int i = 0; i < this.word.length(); i++) {
                Iterator iter = new PermutationGenerator(this.word.substring(0, i) + this.word.substring(i + 1)).getPermutations().iterator();
                while (iter.hasNext()) {
                    result.add(this.word.charAt(i) + ((String) iter.next()));
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        String word = "India";
        PermutationGenerator generator = new PermutationGenerator(word);

        ArrayList<String> results = generator.getPermutations();

        System.out.printf(
        "%s: %c\n%s: %c\n%s: %c\n", 
        results.get(3), results.get(3).charAt(3),
        results.get(10), results.get(10).charAt(3),
        results.get(17), results.get(17).charAt(3));
        System.out.println(results.size());
    }
}
