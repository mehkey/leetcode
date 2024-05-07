class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        tot = 0
        
        l = 0
        r = 0
        
        for c in s:
            
            if c == 'R':
                r += 1
            if c == 'L':
                l += 1
            
            if l == r:
                tot += 1
                l=0
                r=0
        
        return tot