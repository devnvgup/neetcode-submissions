class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = []
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                res.append(prices[j]-prices[i])

        return 0 if all(num < 0 for num in res) else max(res)

       