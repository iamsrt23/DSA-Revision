# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(self, prices: List[int]) -> int:

        n=len(prices)
        buy=prices[0]
        profit = 0

        for i in range(1,n):
                cost = prices[i]-buy
                profit = max(profit,cost)
                buy = min(buy,prices[i])
        return profit