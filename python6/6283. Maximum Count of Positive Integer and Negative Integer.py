class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        p = 0
        neg = 0
        for n in nums:
            if n > 0 :
                p+=1
            if n< 0:
                neg+=1
        
        return max(p,neg)
        
        