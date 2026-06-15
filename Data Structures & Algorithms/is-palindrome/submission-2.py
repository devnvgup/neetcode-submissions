class Solution:
    def isPalindrome(self, s: str) -> bool:
        #wasitacaroracatisaw
        sList = s.split(" ")
        sString = "".join(sList)
        sString = sString.lower()

        sRereseList = sList[::-1]
        print(sRereseList)
        tmp = []
        for i in range(len(sRereseList)):
            revertString = sRereseList[i][::-1]
            print(revertString)
            tmp.append(revertString)
        sRereseString = "".join(tmp)
        sRereseString = sRereseString.lower()
        sString = re.sub(r"[?/<>\.\.\,\'\:]", "", sString)
        sRereseString = re.sub(r"[?/<>\.\.\,\'\:]", "", sRereseString)
        print(sString)
        print(sRereseString)

        if sString == sRereseString : return True
        return False

