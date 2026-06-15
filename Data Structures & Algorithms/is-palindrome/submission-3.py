class Solution:
    def regexSpecialCharacter(self, string:str)->str:
        regexString = re.sub(r"[?/<>\.\.\,\'\:]", "", string)
        return regexString
    def isPalindrome(self, s: str) -> bool:

        #wasitacaroracatisaw
        sList = s.split(" ")
        sString = "".join(sList)
        sString = sString.lower()

        sRereseList = sList[::-1]
        tmp = []
        for i in range(len(sRereseList)):
            revertString = sRereseList[i][::-1]
            tmp.append(revertString)
        sRereseString = "".join(tmp)
        sRereseString = sRereseString.lower()
        sString = self.regexSpecialCharacter(sString)
        sRereseString = self.regexSpecialCharacter(sRereseString)
        if sString == sRereseString : return True
        return False

