class Solution {
    public boolean isAnagram(String s, String t) {
          // check length
        if (s.length() != t.length()) {
            return false;
        }
        Map<Character, Integer> mapS = new HashMap<>();
        Map<Character, Integer> mapT = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            if (!mapS.containsKey(s.charAt(i))) {
                mapS.put(s.charAt(i), 1);
            } else {
                int existValue = mapS.get(s.charAt(i)); 
                mapS.put(s.charAt(i), ++existValue);
            }

        }
        for (int i = 0; i < t.length(); i++) {
            if (!mapT.containsKey(t.charAt(i))) {
                mapT.put(t.charAt(i), 1);
            } else {
                int existValue = mapT.get(t.charAt(i));
                mapT.put(t.charAt(i), ++existValue);
            }

        }
        // jar
        // jam
        if (mapS.size() != mapT.size()) {
            return false;
        }

        for (Map.Entry<Character, Integer> entry : mapS.entrySet()) {
            System.out.println(entry.getKey() + " : " + entry.getValue());
            int value = entry.getValue();
            Character key = entry.getKey();
            System.out.println(mapT.containsKey(key));
            if (!mapT.containsKey(key) || mapT.get(key) != value) {
                return false;
            }

        }

        return true;
    }
}
