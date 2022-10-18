class Solution:
    def equalFrequency(self, word: str) -> bool:
        
        c = Counter(word)
        
        m = c.values()
        
        for l in c:
            c[l] -= 1
            
            i = c[l]
            s = set(c.values())
            if 0 in s:
                s.remove(0)
            v = len(s)
            if v == 1:
                return True
            
            c[l] += 1
        
        return False

        '''
        for l in c:
            if c[l] == m or m == 1:
                c[l] -= m
        
        
        if m > 1:
            return sum(c.values()) == 1
        else:
            return sum(c.values()) == 0 or sum(c.values()) == 1
        
        
        if m == 0:
            return False
        
        for l in c:
            c[l] -= m
        
        
        
        if m > 1:
        
            return sum(c.values()) == 1
        
        else:
            return sum(c.values()) == 0 or sum(c.values()) == 1
        '''
        
        
        