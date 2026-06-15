class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # [1,2,3,4] target = 3 => return index [1,2]

        i = 0
        k = len(numbers) - 1
        while i < len(numbers):
            if i == k: return []
            if numbers[i] + numbers[k] == target: return [i + 1,k + 1]
            elif numbers[i] + numbers[k] > target: k-=1
            elif numbers[i] + numbers[k] < target: i+=1

        