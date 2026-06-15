class Solution:
    def isValid(self, s: str) -> bool:
        # test case : ({{{{}}}))
        hash = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        arr = []
        for i in range(len(s)):
            if hash.get(s[i]) in arr and hash.get(s[i]) == arr[-1]:
                arr.pop()
                continue
            arr.append(s[i])
        if(len(arr) == 0): return True
        return False

    
       
