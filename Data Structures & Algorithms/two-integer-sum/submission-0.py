class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3,4,5,6] target = 7 => output = [0,1]
        # 7-3=4 7-4=3

        #hash[4]
        #hash[7-3]=4
        #hash[7-4]=3
        hash={}
        for i in range(len(nums)):
            if(hash.get(nums[i]) is not None):
                return [hash.get(nums[i]),i]
            else:
                hash[target-nums[i]]= i
