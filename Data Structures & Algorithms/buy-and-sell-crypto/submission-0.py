class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[l] < prices[r]:
                p = prices[r] - prices[l]
                prof = max(prof, p)
            else:
                l = r
            r+=1
        return prof