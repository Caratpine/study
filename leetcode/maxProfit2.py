class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        if prices:
            v = prices[0]
            p = prices[0]
        else:
            return 0
        max_profit = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            v = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            p = prices[i]
            max_profit += p - v
        return max_profit
