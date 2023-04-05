class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        
        
        l = 0
        r = 0
        N = len(s)
        c = 0
        m = 0
        
        def val(ch):
            if ch in chars:
                return vals[chars.index(ch)]
            
            return ord(ch) - ord('a') + 1
            
        while r < N:
            
            c += val(s[r])
            r+=1

            while c < 0 and l < r :
                c -= val(s[l])
                l+=1
            
            m = max(m,c)

        return m