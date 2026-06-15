class Solution {
    public boolean isPalindrome(String s) {
         // Input: s = "Was it a car or a cat I saw?"
        // 2 pointer
        // wasitacaroracatisaw

        // convert to string
       String result = s.trim().toLowerCase().replaceAll("[^a-z0-9]", "");
        // loop string
       
            // j = 0 ; k = len - 1, num = 1
            int j = 0;
            int k = result.length()-1;
            while(j<k){
                if(result.charAt(j)==(result.charAt(k))){
                    j++;
                    k--;
                    continue;
                }
                return false;
            }
            return true;
        
        
        // if s[i] != s[j] return false
        // if j <= k return true
    }
}
