class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        max_profit = 0
        if (prices.index(min(prices)) < prices.index(max(prices))):
            return max(prices) - min(prices)
        else:
            for price in prices:
                buy = min(buy, price)
                max_profit = max(max_profit, price - buy)
            return max_profit