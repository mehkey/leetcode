class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) -1
        
        maxAmount = 0
        
        while(l<r):
            
            maxAmount  = max(maxAmount, min(height[l], height[r])*(r - l))
            if(height[l] >= height[r]):
                r -= 1
            else:
                l +=1
            
        return maxAmount