class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # -1  -1  0  1  2  => [-1,-1,2]  
        # -1 -1 0 1 
        # -2 0 0 2 2
        # [-1,0,1,2,-1,-4] => -4 -1 -1 0 1 2
        nums.sort()
        i = 0
        res = []
        for i in range (len(nums)):
            if i != 0 and nums[i] == nums[i-1] : continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if(nums[i]+nums[j]+nums[k]) == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    while j < len(nums) - 1 and nums[j] == nums[j+1]:
                        j+=1
                    while k > j and nums[k] == nums[k-1]:
                        k-=1
                    j+=1
                    k-=1
                elif (nums[i]+nums[j]+nums[k]) < 0:
                    j+=1
                elif (nums[i]+nums[j]+nums[k]) > 0:
                    k-=1
        return res