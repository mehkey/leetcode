class Solution:
    def countElements(self, nums: List[int]) -> int:
        
        #s = set(nums)
        c = Counter(sorted(nums))
        
        t = 0
        
        for i,k in enumerate(c):
            if i == 0 or i == len(c) -1:
                continue
            
            t += c[k]
            
        
        return t