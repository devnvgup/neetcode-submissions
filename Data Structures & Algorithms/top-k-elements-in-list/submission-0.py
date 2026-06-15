class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [1,2,2,3,3,3] k=2
        # output = [2,3]
        hash = {}
        nums.sort()
        for i in range(len(nums)):
            if(hash.get(nums[i]) is None):
                hash[nums[i]] = 1
            else:
                hash[nums[i]] = hash[nums[i]] + 1
        print(hash)
        sorted_dict = dict(sorted(hash.items(), key=lambda item: item[1], reverse=True))
        print(sorted_dict)
        arrKey = list(sorted_dict.keys())
        return arrKey[:k]
        