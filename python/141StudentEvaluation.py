class Solution:
    def checkRecord(self, s: str) -> bool:
        
        """a = False
        
        for i,c in enumerate(s):
            
            if c == 'A':
                if a:
                    return False
                else:
                    a = True
            
            if c == 'L':
                if i-1 >=0 and s[i-1] == 'L' and i-2 >=0 and s[i-2] == 'L':
                    return False
        
        return True
        
        """
        return s.count('A') <= 1 and s.count('LLL') == 0
