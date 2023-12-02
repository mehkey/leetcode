class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:

        m = float('inf')
        mm = ""
        
        @cache
        def dp(i,prev):
            nonlocal m, mm

            if i == len(s):
                return
            
            if s[i] == '1':
                prev += 1
            
            if prev == k:
                j = i
                cs = 0
                
                while j >= 0:
                    if s[j] == '1':
                        cs += 1
                    if cs == k:
                        break
                    j-=1
                mmm = s[j:i+1]
                #print(mmm)
                if len(mmm) < m:
                    #if mmm < mm or m == float('inf'):
                        mm = mmm
                        m = len(mmm)
                elif len(mmm) == m:
                    if mmm < mm :
                        mm = mmm
                        m = len(mmm)
                return 
            
            dp(i+1,prev)
            return

        

        for i in range(0,len(s)):
            dp(i,0)

        #print(mm)
        
        return mm 



class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:

        for l in range(1, 1+len(s)):
            found = False
            t = None
            for i in range(len(s) - l + 1):
                ss = s[i:i+l]
                ct = ss.count('1')
                if ct == k:
                    found = True
                    if t is None or t > ss:
                        t = ss
            if found:
                return t                
        return ''

        '''
        for i in range(1,len(s)):
            
            for j in range(0,len(s)):
                count = 0
                for k in range(j,min(j+i,len(s))):
                    if s[k] == '1':
                        count += 1
                    if count == kk:
                        return s[j:k+1]
        
        return 
        
        m = float('inf')
        mm = ""
        
        @cache
        def dp(i,prev):
            nonlocal m, mm

            if i == len(s):
                return
            
            if s[i] == '1':
                prev += 1
            
            if prev == k:
                j = i
                cs = 0
                
                while j >= 0:
                    if s[j] == '1':
                        cs += 1
                    if cs == k:
                        break
                    j-=1
                mmm = s[j:i+1]
                #print(mmm)
                if len(mmm) < m:
                    #if mmm < mm or m == float('inf'):
                        mm = mmm
                        m = len(mmm)
                elif len(mmm) == m:
                    if mmm < mm :
                        mm = mmm
                        m = len(mmm)
                return 
            
            dp(i+1,prev)
            return

        

        for i in range(0,len(s)):
            dp(i,0)

        #print(mm)
        
        return mm 
        '''