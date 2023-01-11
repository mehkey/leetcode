class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        
        res = 0
        
        for x in nums:
            res ^= x
            
        #print(res)
            
        return res