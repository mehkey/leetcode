class Solution:
    def countKeyChanges(self, s: str) -> int:
        count = 0
        prev= s[0].upper()
        for c in s.upper():
            
            if c != prev:
                count += 1
            
            prev = c
        
        return count