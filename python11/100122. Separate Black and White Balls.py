class Solution:
    def minimumSteps(self, s: str) -> int:
        
        
        l = 0
        
        res = 0
        
        for c in s:
            if c == '1':
                l += 1
            if c == '0':
                res += l
        
        l = 0
        '''
        for c in s[::-1]:
            if c == '0':
                l += 1
            if c == '1':
                res += l
        '''
        return res
        