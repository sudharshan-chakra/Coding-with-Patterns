class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        length = len(prices)

        for i in range(1,length):
            if prices[i] > prices[i-1]:
                max_profit += (prices[i] - prices[i-1])

        return max_profit