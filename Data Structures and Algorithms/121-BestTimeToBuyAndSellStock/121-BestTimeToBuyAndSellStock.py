# Last updated: 6/4/2026, 6:36:10 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for current in prices[1:]:
            if buy > current:
                buy = current

            profit = max(profit, current - buy)
        
        return profit
