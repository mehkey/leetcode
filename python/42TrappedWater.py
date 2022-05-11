class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0

        r = len(height) - 1

        maxLeft = 0
        
        maxRight = 0
        
        trapped = 0
        
        while( l <= r):
            

            if maxLeft <= maxRight:
                
                trapped = trapped + max( min(maxLeft, maxRight) - height[l], 0)
                maxLeft = max(maxLeft, height[l])
                l += 1

            else:
                trapped = trapped + max( min(maxLeft, maxRight) - height[r], 0)
                maxRight = max(maxRight, height[r])
                r -= 1

        return trapped