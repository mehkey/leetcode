class Solution:
    def minMaxDifference(self, num: int) -> int:
        
        s = str(num)
        
        t = '9'
        
        for c in s:
            if c != '9':
                t = c
                break
                
        high = s.replace(t,'9')
        
        
        s = str(num)
        
        low = s.replace(s[0],'0')
        
        #print(high)
        #print(low)
        return int(high) - int(low)