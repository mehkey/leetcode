class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        t = 0
        s = set()
        
        while nums:
            
            v = nums.pop()
            t += 1
            
            if v <= k:
                s.add(v)
            
            if len(s) == k:
                break
        
        return t