class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        c = Counter(nums)
        
        for n in reversed(sorted(c.keys())):
            
            if n <= 0:
                return -1
        
            if -n in c:
                return n
        
        return -1