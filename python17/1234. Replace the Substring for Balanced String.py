class Solution:
    def balancedString(self, s: str) -> int:
        
        
        counter = collections.Counter(s)
        n = len(s) // 4
        extras = {}
        for key in counter:
            if counter[key] > n:
                extras[key] = counter[key] - n
        
        if not extras: return 0
        i = 0
        res = len(s)
        for j in range(len(s)):
            if s[j] in extras:
                extras[s[j]] -= 1
            
            while i <=j and max(extras.values()) <= 0:
                res = min(res, j-i+1)
                if s[i] in extras:
                    extras[s[i]] += 1
                i += 1
                
                
        return res



        
        c= Counter(s)
        
        tar = len(s)//4
        
        #print(c)
        #qd,ed,wd,rd = abs(tar - c['Q']) , abs(tar - c['E']) , abs(tar - c['W']) , abs(tar - c['R']) 
        qd,ed,wd,rd =  c['Q'] - tar , c['E'] - tar ,  c['W'] - tar ,  c['R'] - tar
        
        if qd < 0:
            qd = 0
        if ed < 0:
            ed = 0
        if wd < 0:
            ed = 0
        if rd < 0:
            rd = 0
        #return diff // 2
        #diff = (qd+ed+wd+rd)
        #print(qd, ed, wd, rd)
        if qd == ed == wd == rd == 0:
            return 0
        #    return 0

        q,e,w,r = 0,0,0,0
        
        ms = len(s)

        N = len(s)
        l = 0
        
        #print('new')
        for r in range(N):
            
            if s[r] == 'Q':
                q += 1
            if s[r] == 'W':
                w += 1
            if s[r] == 'E':
                e += 1
            if s[r] == 'R':
                r += 1
            
            while l <= r and max( ( qd - q if qd > 0 else 0 , wd - w if wd > 0 else 0 , ed - e if ed > 0 else 0 ,rd - r if rd > 0 else 0  ) ) <= 0: #min(  q , qd) + min( w , wd) + min( e , ed) + min(  r , rd) >= diff  :
                
                if  r - l + 1 < ms:
                    #print(l,r)
                    ms = r - l + 1

                if s[l] == 'Q':
                    q -= 1
                if s[l] == 'W':
                    w -= 1
                if s[l] == 'E':
                    e -= 1
                if s[l] == 'R':
                    r -= 1

                l += 1

        return ms 
