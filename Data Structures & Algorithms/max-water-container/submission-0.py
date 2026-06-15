class Solution:
    def maxArea(self, heights: List[int]) -> int:
       # v = h.dict
       # input =  [1,7,2,5,4,7,3,6]  => output = 36

        res = []
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                minH = min (heights[i],heights[j])
                v = minH * (j-i)
                res.append(v)

        res.sort()
        return res[len(res)-1]

        