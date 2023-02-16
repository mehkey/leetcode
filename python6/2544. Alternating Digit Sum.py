class Solution:
    def alternateDigitSum(self, n: int) -> int:
        
        s = str(n)
        
        res = 0
        b = True
        for c in s:
            
            if b:
                res+= int(c)
            else:
                res-= int(c)
            
            b = not b
        
        return res