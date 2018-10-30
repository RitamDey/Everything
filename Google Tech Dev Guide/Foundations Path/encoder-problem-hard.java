import java.util.Map;
import java.util.HashMap;
import java.util.Arrays;


class Solution {
  public String[] encoder(String[] raw, String[] code_words) {
    int pos = 0;
    int code_pos = 0;
    Map<String, String> map = new HashMap<String, String>();
    
    String[] res = new String[raw.length];
    
    for (String chr: raw) {
      if (!map.containsKey(chr))
        map.put(chr, code_words[code_pos++]);
      
      res[pos++] = map.get(chr);
    }

    return res;
  }

  public static void main(String[] args) {
    Solution objSolution = new Solution();

    String[] code = {"1", "2", "3", "4"};
    String[] raw_1 = {"a"};
    String[] raw_2 = {"a", "b"};
    String[] raw_3 = {"a", "b", "a"};
    
    System.out.println(
      Arrays.toString(objSolution.encoder(raw_1, code))
    );
    System.out.println(
      Arrays.toString(objSolution.encoder(raw_2, code))
    );
    System.out.println(
      Arrays.toString(objSolution.encoder(raw_3, code))
    );
  }
}
