class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        
        t = 0
        for r in nums:
            
            r.sort(reverse=True)
        
        for c in zip(*nums):
            
            t += max(c)

        #print(nums)
        
        return t
        
        