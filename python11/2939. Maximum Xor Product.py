

class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        
        t, u = (a >> n)<<n, (b >> n)<<n
        for i in range(n-1, -1, -1):
            aa = (a >> i) & 1
            bb = (b >> i) & 1
            if aa == bb:
                t ^= (1 << i)
                u ^= (1 << i)
            elif t <= u:
                t ^= (1 << i)
            else:
                u ^= (1 << i)

        return (t * u) % (10**9+7)
        
        return r
    
    
        '''
        l = 0
        r = 2**n-1
        
        m = 0
        
        while l <= r:
            
            mid = (l+r) // 2
            
            rr = (a ^ mid) % MOD
            rr = rr * ((b ^ mid) % MOD ) % MOD

            if mid >= 
        
        
        a = 12 =    1100
        b = 5  =     101
        
                      11 = 3
                    1111 = 15
                     110 = 6
                         = 90
                         
                      10
                    1110 = 14
                     111 = 7
                         = 98

                  14 * 7
                  15 * 
                     
                      (0 and 16)
        
        a = 6 =.     110
        b = 7 =.     111
        
        
                00011001
                    (0 and 32)
                
                    1
                  110
                  101
                   
                  100
                  011
                  
                    (0 and 8)
   
        
        
        MOD = 10**9+7
        
        #def dp(idx):
        #aa = bin(a)[::-1]
        #ma = len(aa)
        #bb = bin(b)[::-1]
        #mb = len(bb)
        
        @cache
        def dp(idx, cur):
            
            if idx == n:
                
                r = (a ^ cur) * ((b ^ cur)  ) 

                return r
            
            #if a & (1 << idx) == 0 and a & (1 << idx) == 0:
            #    return dp(idx+1,cur | 1 << idx)
            
            #if a & (1 << idx) == 1 and a & (1 << idx) == 1:
            #   return dp(idx+1,cur )

            return max(dp(idx+1,cur | 1 << idx), dp(idx+1,cur) ) 
            
        
        return dp(0,0) % MOD
        
        '''
        
        MOD = 10**9+7
        
        '''
        aa = bin(a)[::-1]
        ma = len(aa)
        bb = bin(b)[::-1]
        mb = len(bb)
        
        res = 0
        #print(aa,bb)
        for i in range(0,min(ma,mb,n+2)-2):
            
            #aaa = a
            if aa[i] == '0' and bb[i] == '0':
                res |= 1 << i
        
        #print(max(ma,mb)-2, n )
        for i in range(max(ma,mb)-2,n):
            res |= 1 << i
        
        #print(res)
        
        r = (a ^ res) % MOD
        r = r * ((b ^ res) % MOD ) % MOD
        '''
        
        MOD = 10**9+7
        
        
        aa = bin(a)[::-1]
        ma = len(aa)
        bb = bin(b)[::-1]
        mb = len(bb)
        

        t, u = (a >> n)<<n, (b >> n)<<n
        for i in range(n-1, -1, -1):
            aa = (a >> i) & 1
            bb = (b >> i) & 1
            
            if aa == bb:
                t |= (1<<i)
                u |= (1<<i)
            elif t >= u:
                u |= (1 << i)
            else:
                t |= (1 << i)
        
        return ( t * u ) % MOD
        
        
        
        t, u = (a >> n)<<n, (b >> n)<<n
        for i in range(n-1, -1, -1):
            aa = (a >> i) & 1
            bb = (b >> i) & 1
            if aa == bb:
                t ^= (1 << i)
                u ^= (1 << i)
            elif t <= u:
                t ^= (1 << i)
            else:
                u ^= (1 << i)

        return (t * u) % (10**9+7)
        
        return r
        
        
        