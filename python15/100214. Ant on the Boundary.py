class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        
        cur = 0
        res = 0
        for ch in nums:
            
            cur += ch
            
            if cur == 0:
                res += 1
                
        return res