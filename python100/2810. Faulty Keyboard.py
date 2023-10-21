class Solution:
    def finalString(self, ss: str) -> str:
        
        s = []
        
        for c in ss:
            
            if c == 'i':
                s = s[::-1]
            else:
                s.append(c)
        
        return ''.join(s)