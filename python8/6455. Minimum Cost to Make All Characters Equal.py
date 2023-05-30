class Solution:
    def minimumCost(self, s: str) -> int:
        

        n = len(s)
        
        c = 0

        for i in range(1,len(s)):

            if s[i] != s[i-1] :
                c += min(i, n-i)
        
        return c
                