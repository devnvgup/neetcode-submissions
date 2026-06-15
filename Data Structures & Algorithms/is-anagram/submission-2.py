class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        # racecar  
        # carrace
        hashtable = {}
        for i in range(len(s)):
            countTime = s.count(s[i])
            hashtable[s[i]] = countTime
        for i in range(len(t)):
            countTime = t.count(t[i])
            if(t[i] not in hashtable or hashtable[t[i]] != countTime):
                return False
            else:
                continue

        return True    

    
        