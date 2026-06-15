class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def filterOutAndCheckDuplicate(listArr:List[[str]])->bool:
            filterOutEmtyString = list(filter(lambda x: x != ".", listArr))
            duplicates = list(set([x for x in filterOutEmtyString if filterOutEmtyString.count(x) > 1]))
            if len(duplicates) > 0 : return False
            return True

        def checkValidSudoKu(range1: str, range2: str)->bool:
            convertRange1 = tuple(map(int, range1.split(',')))
            convertRange2 = tuple(map(int, range2.split(',')))
            tmp = []
            for i in range (*convertRange1):
                for j in range (*convertRange2):
                    tmp.append(board[i][j])
                    print(board[i][j])
            isNotDuplicate = filterOutAndCheckDuplicate(tmp)
            return isNotDuplicate
        #[
        #   [1,2,",",3,",",","]
        #   [4,5,",",",",",","]
        #   [",9,8,",",",",",3]
        #   [5,",",",6,",",",4]
        #   [",",",8,",3,",",5]
        #   [7,",",",2,",",",6]
        #   [",",",",",",2,","]
        #   [",",",4,1,9,",",8]
        #   [",",",",8,",",7,9]
        #]
        # => output = true valid sudoku


        # Each row must contain the digits 1-9 without duplicates
        # Each column must contain the digits 1-9 without duplicates.
        # Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

        #loop row
        for i in range (9):
            tmp = []
            for j in range (9):
                if board[i][j] != ".":
                    tmp.append(board[i][j])

            duplicates = set([x for x in tmp if tmp.count(x) > 1])
            if len(duplicates) > 0 : return False

                


        #loop col
        for i in range (9):
            tmp = []
            for j in range (9):
                if board[j][i] != ".":
                    tmp.append(board[j][i])

            duplicates = set([x for x in tmp if tmp.count(x) > 1])
            if len(duplicates) > 0 : return False

        #loop 3x3 sub-boxes
        # loop boxes1:
        isBoxed1Valid = checkValidSudoKu("0,3","0,3")
        if not isBoxed1Valid : return False
        #loop boxes2:
        isBoxed2Valid = checkValidSudoKu("0,3","3,6")
        if  not isBoxed2Valid : return False
        # loop boxes3:
        isBoxed3Valid = checkValidSudoKu("0,3","6,9")
        if not isBoxed3Valid : return False
        # loop boxes4:
        isBoxed4Valid = checkValidSudoKu("3,6","0,3")
        if not isBoxed4Valid: return False
        # loop boxes5:
        isBoxed5Valid = checkValidSudoKu("3,6","3,6")
        if not isBoxed5Valid : return False
        # loop boxes6:
        isBoxed6Valid = checkValidSudoKu("3,6","6,9")
        if not isBoxed6Valid : return False
        # loop boxes7:
        isBoxed7Valid = checkValidSudoKu("6,9","0,3")
        if not isBoxed7Valid : return False
        # loop boxes8:
        isBoxed8Valid = checkValidSudoKu("6,9","3,6")
        if not isBoxed8Valid : return False
        # loop boxes9:
        isBoxed9Valid = checkValidSudoKu("6,9","6,9")
        if not isBoxed9Valid : return False
        return True


