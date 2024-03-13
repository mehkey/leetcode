class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        d = {}
        r = -1
        for i,c in enumerate(s):

            if d.get(c,-1) != -1:
                r = max(r, i - d.get(c) - 1)
            
            else:
                d[c] = i
        
        return r