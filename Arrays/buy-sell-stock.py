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


def maxProfit_2(self, prices: List[int]) -> int:
        
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                  min_price = price
            elif price-min_price > max_profit:
                  max_profit = price-min_price
        return max_profit
        