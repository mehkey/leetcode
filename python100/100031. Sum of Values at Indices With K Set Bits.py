class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        
        t = 0
        for i in range(len(nums)):
            tt = bin(i).count("1")
            
            if tt == k:
                t += nums[i]
        
        return t