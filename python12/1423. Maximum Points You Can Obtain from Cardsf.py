class Solution:
    def maxScore(self, cp: List[int], k: int) -> int:
        
        '''
        l = 0
        n = len(cp)
        r = n-1
        t = 0
        kk = 0

        while l <= r:

            if cp[l] >= cp[r]:
                t += cp[l]
                l+=1
            else:
                t += cp[r]
                r-=1
                
            kk+=1
            if kk == k:
                break
        return t
        '''
        n = len(cp)
        lp = [0]*n
        lr = [0]*n
        
        for i in range(0,n):
            lp[i] = cp[i] + lp[i-1]
        
        for i in range(n-1,-1,-1):
            lr[i] = cp[i] + ( lr[i+1] if i+1 < n else 0)
            
        m = 0
        
        j = 0
        #print(lp,lr)
        
        for i in range(k-1,-1,-1):
            #print(i,n-1,n-1-j)
            #print(lp[i] , lp[n-1] , lp[n-1-j])
            tot = lp[i] + lp[n-1] - lp[n-1-j]
            m = max(m, tot)
            j+=1
        m = max(m, lp[n-1] - lp[n-1-j])

        return m
        #print(lp,lr)