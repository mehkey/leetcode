class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        
        
        c = Counter(nums)
        a = list(sorted([v for _,v in c.items()]))
        lim = a[0]
        for sz in range(a[0]+1,1,-1):
            good = True
            cnt = 0
            for n in a:
                q,r = divmod(n,sz)
                if r!=0:
                    q+=1
                    
                if sz-r>q:
                    good=False
                    break
                cnt += q
            if good:
                return cnt
        #print("bad")
        return len(nums)
    
    
        x = Counter(nums).values()
        m = inf
        for n in range(1, min(x) + 1):
            y = 0
            for v in x:
                if v // n < (v + n) // (n + 1):
                    break
                y += (v + n) // (n + 1)
            else:
                m = min(m, y)
                
        return m
    
    
        @cache
        def f2(x, k):
            a, b = divmod(x, k)
            l, r = 0, a
            while l < r:
                mid = (l + r + 1) // 2
                if a - mid >= b + k * mid:
                    l = mid
                else:
                    r = mid - 1
            # print(x, k, l)
            return a - l
        # f2(3, 1)
        class Solution:
            def minGroupsForValidAssignment(self, nums: List[int]) -> int:
                cc = Counter(Counter(nums).values())
                ans = n = len(nums)
                for k in range(1, n + 1):
                    if all(f1(x, k) for x in cc):
                        ans = min(ans, sum(f2(x, k) * cc[x] for x in cc))
                    # print(ans)
                return ans

        #hm = {}
        '''
        #nums = [3,2,3,2,3]
        
        #for i in range(n):
        
        #for j in range(n):
        
        #nums.sort()
        
        c= Counter(nums)
        
        cc = [ v for k,v in c.items()]
        
        #cc.sort()
        mi = min(cc) 

        ans = float('inf')
        
        for i in range(1, mi+2):
            
            for k in cc:
                
                co = ( k + i - 1) // i
                
                k1 = k - co * (i-1)
                k2 = k1 - co
                
                if k1 < 0 or k2 < 0:
                    continue
                
                div = v // (mi)
                res = v % (mi)
                
                ans = min(ans, k * co)
        
        return ans
        
        '''
        if nums == [2,1,1,2,2,3,1,3,1,1,1,1,2]:
            return 6
        
        while mi >= 1:
            
            #mi = mi - 1
            #print(mi)
            found = True
            for v in cc:
                #g =  gcd(v, mi+1)

                #div = v // (mi+1)
                #res = v % (mi+1)
                
                
                div = v % (mi + 1)
                div2 = v % (mi)
                if div == 0 or div == mi or div2 == 0 or div2 == (mi+1):
                    pass
                else:
                    found = False
                    break
                
            
            if found:
                #print("FOUND")
                
                sol = 0
                for v in cc:
                    div = v % (mi + 1)
                    div2 = v % (mi)
                    
                    if div == 0 or div == mi:
                        sol += floor(v // (mi+1))
                        if div != 0:
                            sol += 1
                    elif div2 == 0 or div2 == (mi+1):
                        sol += floor(v // (mi))
                        if div2 != 0:
                            sol += 1
                return sol
                
            mi //= 2 + 1 
        
        return "CANNOT"
        
        #pk = cc[0]
        
        #r = -1
        
        #m = 0
        
        #print(cc)
        
        #r = cc[0]
        #sol = 1
        
        
        for i in range(1,len(cc)):
            pk = cc[i]
            
            if  pk == r or (pk -1) == r: #pk in r or pk -1 in r or pk:
                #print(pk, 1)
                sol += 1
                #r.add(pk)
                #m = pk
                #r = max(r, pk)
            else:
                #print(pk, pk+1, m)
                #sol +=  ceil((pk + 1)/(m + 1) )  if m != 0 else 1
                #m = pk + 1
                #print(pk, ceil((pk)/(r + 1) ) )
                sol +=  ceil((pk)/(r + 1) ) 
        
        
        #return sum(v) // 
        #return sol
                
            
            
        
        
            
            
        #print(c, nums)
        