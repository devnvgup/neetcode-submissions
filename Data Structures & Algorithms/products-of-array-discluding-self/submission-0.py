class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # [1,2,4,6] => [48,24,12,8]
        i = 0
        res = []
        while(i<len(nums)):
            multiply = 1
            k=0
            while(k<len(nums)):
                if i == k:
                    k+=1
                    continue

                multiply *= nums[k]
                k+=1
            res.append(multiply)
            i+=1

        return res
                

        