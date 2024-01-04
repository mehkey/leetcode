class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        
        cs = 0
        
        ctot = 0
        
        ma = -1

        for n in nums:

            if ctot >= 2 and cs > n:
                ma = max(ma, cs+n)
            
            ctot += 1
            cs += n


        return ma
        