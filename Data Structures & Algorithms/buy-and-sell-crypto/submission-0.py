class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        best = 0

        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            elif prices[r] - prices[l] > best:
                best = prices[r] - prices[l]

        return best
