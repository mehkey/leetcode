class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        MOD = 10**9 + 7

        cur = [(e,s,i) for i,(s,e) in enumerate(zip(speed,efficiency))]
        
        cur.sort(reverse=True)
        
        ss = 0
        c = 0

        tot =0 
        h = []
        
        #print(cur)
        
        for e,s,i in cur:
            c+= 1
            if c <= k:
                ss += s
                tot = max(ss * e, tot)
                heappush(h,s)

            else:
                heappush(h,s)
                cc = heappop(h)
                ss += s
                ss -= cc
                tot = max(tot, ss * e)
            
            
        return tot % MOD
        
        '''
        s = 0
        c = 0
        m = float('inf')

        def dp(i):
            nonlocal c
            nonlocal s
            nonlocal m
            
            if c == k:
                return ( s * m )
            
            if i == len(speed):
                return float('-inf')

            prevm = m
            
            first = dp(i+1)
            
            m = prevm
            
            s += speed[i]
            m = min(m,efficiency[i])
            c += 1
            second = dp(i+1)
            c -= 1
            s -= speed[i]

            m = prevm

            return max( first, second) 
        
        return dp(0)  % (10**9+7)
        '''