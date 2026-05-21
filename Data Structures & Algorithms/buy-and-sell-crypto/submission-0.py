class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        price = prices[0]

        for i in range(1,len(prices)):
            
            price = min(price, prices[i])
            
            profit = max(profit, prices[i]-price)

        return profit

        