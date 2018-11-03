class Solution {
    public String withoutString(String base, String remove) {
        char remove_0 = remove.charAt(0);
        String res = "";

        for (int pos=0; pos < base.length(); ++pos) {
            if (base.charAt(pos) == remove_0 && base.regionMatches(true, pos, remove, 0, remove.length())) {
                System.out.println("Inside");
                pos += remove.length();

                if (remove.length() > 1)
                    pos += 1;
                continue;
            }

            res += base.charAt(pos);
        }

        return res;
    }

    public static void main(String[] args) {
        Solution obj = new Solution();

        System.out.println(obj.withoutString("This is a FISH", "is"));
        System.out.println(obj.withoutString("xyzzy", "Y"));
        System.out.println(obj.withoutString("Hello there", "x"));
    }
}
