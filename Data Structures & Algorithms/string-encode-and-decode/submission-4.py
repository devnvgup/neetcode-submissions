class Solution:

    # [] => [""] => bug
    # ["","",""] => ",,,"
    # tc3 : ["1,23","45,6","7,8,9"] => ["1,23","45,6","7,8,9"]

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0 : return "empty"
        for i in range(len(strs)):
            if strs[i] == "":
                strs[i] = "space"
        endocer = ""
        for i in range(len(strs)):
            endocer +=  "-" + strs[i]
        return endocer

        

    def decode(self, s: str) -> List[str]:
        if s == "empty": return []
        arr = s.split('-')
        for i in range(len(arr)):
            if(arr[i]=="space"):
                arr[i]=""

        return arr[1:]