class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
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
        tmp1=[]
        for i in range (3):
            for j in range (3):
                tmp1.append(board[i][j])
        filterOutEmtyString = list(filter(lambda x: x != ".", tmp1))
        duplicates = set([x for x in filterOutEmtyString if filterOutEmtyString.count(x) > 1])
        if len(duplicates) > 0 : return False

        # loop boxes2:
        tmp2=[]
        for i in range (3):
            for j in range (3,6):
                tmp2.append(board[i][j])
        filterOutEmtyString = list(filter(lambda x: x != ".", tmp2))
        duplicates = set([x for x in filterOutEmtyString if filterOutEmtyString.count(x) > 1])
        if len(duplicates) > 0 : return False
        # loop boxes3:
        tmp3 = []
        for i in range (3):
            for j in range (6,9):
                tmp3.append(board[i][j])
        filterOutEmtyString = list(filter(lambda x: x != ".", tmp3))
        duplicates = set([x for x in filterOutEmtyString if filterOutEmtyString.count(x) > 1])
        if len(duplicates) > 0 : return False


        # loop boxes4:
        tmp4 = []
        for i in range (3,6):
            for j in range (3):
                tmp4.append(board[i][j])
        filterOutEmtyString = list(filter(lambda x: x != ".", tmp4))
        duplicates = set([x for x in filterOutEmtyString if filterOutEmtyString.count(x) > 1])
        if len(duplicates) > 0 : return False
        # loop boxes5:
        tmp5 = []
        for i in range (3,6):
            for j in range (3,6):
                tmp5.append(board[i][j])
        filterOutEmtyString = list(filter(lambda x: x != ".", tmp5))
        duplicates = set([x for x in filterOutEmtyString if filterOutEmtyString.count(x) > 1])
        if len(duplicates) > 0 : return False
        # loop boxes6:
        tmp6 = []
        for i in range (3,6):
            for j in range (6,9):
                tmp6.append(board[i][j])
        filterOutEmtyString = list(filter(lambda x: x != ".", tmp6))
        duplicates = set([x for x in filterOutEmtyString if filterOutEmtyString.count(x) > 1])
        if len(duplicates) > 0 : return False


        # loop boxes7:

        tmp7 = []
        for i in range (6,9):
            for j in range (3):
                tmp7.append(board[i][j])
        filterOutEmtyString = list(filter(lambda x: x != ".", tmp7))
        duplicates = set([x for x in filterOutEmtyString if filterOutEmtyString.count(x) > 1])
        if len(duplicates) > 0 : return False
        # loop boxes8:

        tmp8 = []
        for i in range (6,9):
            for j in range (3,6):
                tmp8.append(board[i][j])
        filterOutEmtyString = list(filter(lambda x: x != ".", tmp8))
        duplicates = set([x for x in filterOutEmtyString if filterOutEmtyString.count(x) > 1])
        if len(duplicates) > 0 : return False
        # loop boxes9:


        tmp9 = []
        for i in range (6,9):
            for j in range (6,9):
                tmp9.append(board[i][j])
        filterOutEmtyString = list(filter(lambda x: x != ".", tmp9))
        duplicates = set([x for x in filterOutEmtyString if filterOutEmtyString.count(x) > 1])
        if len(duplicates) > 0 : return False


        return True


