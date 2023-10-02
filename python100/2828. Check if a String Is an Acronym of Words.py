class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        
        l = []
        
        for ss in words:
            
            l.append(ss[0])
        
        return ''.join(l) == s
        '''
        for c in s:
            
            if c in l:
                l.remove(c)
        
            else:
                return False
        
        print(l)
        
        return len(l) == 0
        '''