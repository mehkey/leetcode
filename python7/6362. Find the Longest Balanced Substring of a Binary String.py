class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        
        tt = 0
        N = len(s)
        #if all([c =='0' for c in s]):
        #    return 0
        for i,c in enumerate(s):
            
            if c == '0':
                j = i
                cc = 0
                ma = 0
                while j < N and s[j] =='0' :
                    j+=1
                    cc+=1
                    ma += 1
                while j < N and s[j] == '1' and ma > 0:
                    j+=1
                    cc+=1
                    ma -=1
                if ma == 0:
                    tt = max(tt, cc)
        
        return tt
                
                
                
        '''
        zero =True
        
        t = 0
        
        tt = 0
        for c in s:
            
            if zero:
                if c == '0':
                    t+=1
                if c == '1':
                    t+=1
                    zero = False
            if not zero:
                if c == '0':
                    t = 1
                    zero = True
                if c == '1':
                    t+=1
            
            tt = max(tt,t)

        return t
    
        #exaltation
        '''