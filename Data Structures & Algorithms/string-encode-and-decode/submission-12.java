class Solution {

    // Input: dummy_input = ["Hello","World"]

    // Output: ["Hello","World"]

    public String encode(List<String> strs) {
// check if list empty, return empty strs
        if (strs.isEmpty())
            return "";
        // loop to encode
        String encode = "";
        for (String str : strs) {
            encode += str.length() + ",";
        }
        encode += "#";
        for (String str : strs) {
            encode += str;
        }
        return encode;
    }

    public List<String> decode(String str) {
// check if str is empty, return emty arrr
        if (str.isEmpty())
            return new ArrayList<>();
        // loop to decode
        List<String> decode = new ArrayList<>();
        // String l = "";
        List<String> l = new ArrayList<>();
        int k = 0;
        String s = "";
        for (int i = 0; i < str.length(); i += 1) {
            // int l = (str.charAt(i - 1)) - '0';
            // String subString = str.substring(i + 1 , i + 1 + l);
            // decode.add(subString);
            // i = i + l;
            // if (str.charAt(i) != '#') {
            // l += str.charAt(i);
            // } else {
            // String subString = str.substring(i + 1, i + 1 + Integer.parseInt(l));
            // decode.add(subString);
            // i = i + Integer.parseInt(l);
            // l = "";
            // }
            if (str.charAt(i) == '#') {
                while (k < l.size()) {
                    String subString = str.substring(i + 1, i + 1 + Integer.parseInt(l.get(k)));
                    decode.add(subString);
                    i = i + Integer.parseInt(l.get(k));
                    k++;
                }
                break;
            }
            if (str.charAt(i) != ',') {
                // add size
                s+= str.charAt(i);
                
            } else {
                l.add(s);
                s="";
            }

        }
        return decode;
    }
}
