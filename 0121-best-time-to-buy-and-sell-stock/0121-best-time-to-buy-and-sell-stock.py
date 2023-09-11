class Solution:
    def maxProfit(self,prices):
        buy = 0
        sell = 1
        result = 0
        while sell < len(prices):
            currentProfit = prices[sell] - prices[buy] #our current Profit
            if prices[buy] < prices[sell]:
                result =max(currentProfit,result)
            else:
                buy = sell
            sell += 1
        return result