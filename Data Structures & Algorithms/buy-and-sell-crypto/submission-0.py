class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mini , result = prices[0] , 0
        for i in range(1,len(prices)):
            mini = min(mini,prices[i])
            result = max(result,prices[i]-mini)
        return result  