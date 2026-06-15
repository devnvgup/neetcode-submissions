class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashtable = {}
        isDuplicate = False
        i = 0
        max = 10000
        while(i <= len(nums) - 1):
            target = max-nums[i]
            if(hashtable.get(target) is not None):
              isDuplicate = True
              break
            hashtable[max-nums[i]] = max-nums[i]
            i+=1
        return isDuplicate or False