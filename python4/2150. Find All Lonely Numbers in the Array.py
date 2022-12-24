class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        
        s = set(nums)
        c = Counter(nums)
        
        res = []
        
        for n in s:
            
            if c[n] == 1 and n+1 not in s and n-1 not in s:
                res.append(n)
        
        return res