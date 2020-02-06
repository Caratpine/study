from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices:
            min = prices[0]
        else:
            return 0
        max_profit = 0
        for p in prices:
            if p < min:
                min = p
            elif p - min > max_profit:
                max_profit = p - min
        return max_profit

