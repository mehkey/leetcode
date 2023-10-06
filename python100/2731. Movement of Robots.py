class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        
        '''
        
            -2 0 2
            R L L
          .   .   .
          
            .
            .   .
            
          .   .
              .
              
        .   .   .
      .   .       .
        
        
        '''
        sk = {}
        slr = {}
        
        mod = 10**9+7

        r = list()
        l = list()

        for i in range(len(nums)):
            sk[nums[i]] = s[i]

            if s[i] == "L":
                l.append(nums[i])
            if s[i] == "R":
                r.append(nums[i])
        
        res = 0
        ssl = 0
        ssr = 0

        #for v in l:
        #    ssl += v % mod
        
        #for v in r:
        #    ssr += r % mod

        for i,v in enumerate(l):
            #l[i] += v % mod
            l[i] -= d % mod
            #skr[l[i]] = 'l'
        
        for i,v in enumerate(r):
            #res += v  % mod
            r[i] += d % mod
            #skr[r[i]] = sk[v]
        
        l.sort()
        r.sort()
        
        lp = 0
        rp = 0
        
        res = []
        
        while lp < len(l) and rp < len(r):
            if l[lp] < r[rp]:
                res.append(l[lp])
                lp+=1
            else:
                res.append(r[rp])
                rp+=1
        while lp < len(l) :
            res.append(l[lp])
            lp+=1
        
        while rp < len(r):
            res.append(r[rp])
            rp+=1
        
        resp = 0
        
        for i,v in enumerate(res):
            resp = (resp - (v * (len(res)-i))% mod) % mod
        
        for i,v in enumerate(res[::-1]):
            resp = (resp + (v * (len(res)-i))% mod) % mod

        return resp
    

    for i in range(len(s)):
            if s[i] == 'L':
                nums[i] -= d
            else:
                nums[i] += d
                
        ans = 0
        nums.sort()
        mod = 10 ** 9 + 7
        s = 0
        
        for i in range(len(nums)):
            ans += (nums[i] * i - s)
            s += nums[i]
            ans %= mod
            s %= mod
        
        return ans % mod
        '''
            
                
        
        
        sl = sum(l)
        sr = sum(r)
        
        #print(l)
        #print(r)
        for i,v in enumerate(l):
            res -= v * (len(l)-i)
        
        for i,v in enumerate(l[::-1]):
            res += v * (len(l)-i)
        
        for i,v in enumerate(r):
            res -= v * (len(r)-i)
        
        for i,v in enumerate(r[::-1]):
            res += v * (len(r)-i)
        
        prev = 0
        aggr = []
        for v in r:
            aggr.append(prev+v)
            prev = prev+v
        
        for i,v in enumerate(l):
            lefti = bisect_left(r,v)
            #print(lefti)
            res -= v * (lefti+1)
            res += aggr[lefti]
            #print('=',(lefti+1))
            res += v * (len(r) - lefti-1)
            #print( '-',(len(r) - lefti-1))
            res -= aggr[len(r) - lefti-1] - aggr[lefti]
            
        #for i,v in enumerate(r):
        #    res += v *
        
        #for i,v in enumerate(r):
        #    res -= v 

        return res
        '''