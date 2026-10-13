class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_buy = float('inf')

        for p in prices:
            min_buy = min(min_buy, p)
            profit = max(profit, p - min_buy)

        return profit

        