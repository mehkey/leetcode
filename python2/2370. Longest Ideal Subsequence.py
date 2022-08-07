class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        
        s = [ord(c) - ord('a') for c in s]
        
        m = 0
        
        hm = {}
        
        for i,v in enumerate(s) :
            
            m = 1
            for h in hm:
                if abs(v - h) <= k:
                    m = max(m, hm[h] +1)
            
            hm[v] = m
        
        return max(hm.values())