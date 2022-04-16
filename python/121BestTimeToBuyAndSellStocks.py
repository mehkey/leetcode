class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r = 1
        maxProfit = 0
        
        while r < len(prices):
            
            maxProfit = max(maxProfit, prices[r] - prices[l])
            
            while l<r and prices[r] - prices[l] < 0:
                l+=1
            
            r+=1
        
        return maxProfit