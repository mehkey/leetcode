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



        class Solution:


    def maxProfit(self, prices: List[int]) -> int:
        
        
        minimum = float("inf")
        
        maximumdiff = float("-inf")
        
        for p in prices:
            
            if p - minimum > 0:
                maximumdiff = max(maximumdiff, p - minimum)
            
            minimum = min(minimum, p)

        return maximumdiff  if maximumdiff != float("-inf") else 0