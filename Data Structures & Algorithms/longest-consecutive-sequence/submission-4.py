class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = list(dict.fromkeys(nums))
        unique.sort()
        if len(unique) == 0 : return 0
        if len(unique) == 1: return 1
        # # [2,3,4,5,10,20] => [2,3,4,5] => seq = 4
        # #loop
        # #arr push
        # #sort and get bigest index
        i=0
        count = 1
        arr = []
        while i < len(unique):
            if i  == len(unique) - 1 : break
            if unique[i] == unique[i+1] - 1:
                count+=1
            else:
                print(123)
                count = 1
            arr.append(count)
            print(arr)
            i+=1

        arr.sort()
        return arr[len(arr)-1]