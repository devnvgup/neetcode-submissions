class Solution:
    def trap(self, height: List[int]) -> int:
        #  [
        #      [o,o,o,x,o,o,o,x,o,o]       
        #      [o,x,o,x,o,o,o,x,x,o]    => => count = 9
        #      [o,x,o,x,x,o,x,x,x,x]     
        #  ]
        # index x line 1: 3,7 => 7-3-1 =3
        # index x line 2 : 1,3,7,8 => 3-1-1=1
        #                             7-3-1=3
        #                             8-7-1=0
        # index x line 3 : 1,3,4,6,7,8,9 => 3-1-1=1
                                            #4-3-1=1
        #total = 3+4+2=9

        w = len(height)
        h = max(height)


        matrix = [[0] * w for _ in range(h)]
        for i in range(w):
            count = h
            for j in range(h):
                if count <= height[i]:
                    matrix[j][i] = 1
                count-=1

        total=0        
        for i in range(h):
            tmp = []
            for j in range(w):
                if(matrix[i][j]) == 1:
                    tmp.append(j)
            tmp.sort(reverse=True)
            for k in range(len(tmp)):
                if k+1 >= len(tmp) : break
                num = tmp[k] - tmp[k+1] - 1
                total+=num


        return total









