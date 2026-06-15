class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       count = 1
       for i in range(len(nums)):
         count = nums.count(nums[i])
         if count > 1: return True
       return False