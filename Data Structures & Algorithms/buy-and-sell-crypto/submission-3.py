class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        R = 1
        current_max_profit = float("-inf")
        min_left_number = float("inf")

        for L in range(len(prices)):
            if prices[L] > min_left_number:
                R = min(len(prices) - 1, L + 1)
                continue
            while R <= len(prices) - 1:
                current_max_profit = max(prices[R] - prices[L], current_max_profit)
                R = min(len(prices), R + 1)
            R = min(len(prices) - 1, L + 1)
            min_left_number = prices[L]
        return 0 if current_max_profit <= 0 else current_max_profit

