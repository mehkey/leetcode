class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        c = Counter(nums)
        
        m = max(c.values())
        res = 0
        for k,v in c.items():
            if v == m:
                res+=m
            
        return res