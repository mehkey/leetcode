class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        
        
        lo, hi, n = min(stations), sum(stations) + k + 1, len(stations)
        
        def need(target):
            array, total, i, ans = deque(), 0, -1, 0
            for i in range(r):
                array.append(stations[i])
                total += stations[i]
            for i in range(n):
                if i + r < n:
                    array.append(stations[i + r])
                    total += stations[i + r]
                diff = target - total
                if diff > 0:
                    array[-1] += diff
                    total += diff
                    ans += diff
                if i >= r:
                    total -= array.popleft()
            return ans
        
        ma = 0
        while lo <= hi:
            mi = (lo + hi )// 2
            if need(mi) <= k:
                ma = max(ma,mi)
                lo = mi + 1
            else:
                hi = mi - 1
        return ma
        
        n = len(stations)
        init = sum(stations[:r + 1])
        
        '''def can(target):
            i = 0
            rest = k
            cur = init
            plus = {}
            #print(target)
            while i < n:
                #print(i, cur, rest)
                print(cur)
                if cur < target:
                    diff = target - cur
                    if rest < diff:
                        return False
                    rest -= diff
                    cur += diff
                    plus[i + r] = diff
                if i + r + 1 < n:
                    cur += stations[i + r + 1]
                if i - r >= 0:
                    cur -= stations[i - r]
                    if i - r in plus:
                        cur -= plus[i - r]
                i += 1
            return True
        '''
        def can(target):
            array, total, i, ans = deque(), 0, -1, 0
            for i in range(r):
                array.append(stations[i])
                total += stations[i]

            for i in range(n):
                if i + r < n:
                    array.append(stations[i + r])
                    total += stations[i + r]
                diff = target - total
                if diff > 0:
                    array[-1] += diff
                    total += diff
                    ans += diff
                if i >= r:
                    total -= array.popleft()
                if ans > k:
                    return ans
            return ans
            
        mx = sum(stations) + k
        ll, rr = 0, mx + 1
        while rr - ll > 1:
            m = (rr + ll) // 2
            if can(m):
                ll = m
            else:
                rr = m
            
            #print(' -=------------ ')
        return ll
        #for k in range(k):
            
        #kk = power stations for current city
        
        # = power station for next city
        
        #if r == 0:
        #    return min(stations)
        n = len(stations)
        init = sum(stations[:r + 1])
        def can(target):
            i = 0
            rest = k
            cur = init
            plus = {}
            #print(target)
            while i < n:
                #print(i, cur, rest)
                if cur < target:
                    diff = target - cur
                    if rest < diff:
                        return False
                    rest -= diff
                    cur += diff
                    plus[i + r] = diff
                if i + r + 1 < n:
                    cur += stations[i + r + 1]
                if i - r >= 0:
                    cur -= stations[i - r]
                    if i - r in plus:
                        cur -= plus[i - r]
                i += 1
            return True
        
        l = 0
        
        r = sum(stations) + k
        
        ma = 0
        while l < r:
            m = (l+r)//2
            
            if can(m):
                ma = max(ma, m)
                l = m + 1
            else:
                r = m 
        
        return ma
        
        '''
        st=0
        end=10**15
        
        summ1 =0
        #for i in range(r):
        #    summ1+=arr[i]
        n=len(stations)
        while st<=end:
            mid=(st+end)/2
            summ=0
            arr=stations[:]
            c=0
            for i in range(r):
                summ+=arr[i]
            #print(summ)
            for i in range(n):
                if i>r:
                    summ-=arr[i-r-1]
                if i+r<n:
                    summ+=arr[i+r]
                if summ<mid:
                    x=mid-summ
                    c+=x
                    if i+r<n:
                        arr[i+r]+=x
                    else:
                        arr[n-1]+=x
                    summ+=x
            if c<=k:
                st=mid+1
            else:
                end=mid-1
        return math.floor(end)
        
        
        tot = [i for i in stations]
        prev = 0
        q = Deque()
        rr = 0
        for i,n in enumerate(stations):
            
            
            tot[i] += prev
            
            q.append(n)
            prev+= n
            
            if rr != r:
                rr+=1
            else:
                prev -= q.popleft()

        

        prev = 0
        q = Deque()
        rr = 0
        for i in range(len(stations)-1,-1,-1):
            
            n = stations[i]
            tot[i] += prev
            
            q.append(n)
            prev+= n
            
            if rr != r:
                rr+=1
            else:
                prev -= q.popleft()

        
        def calculate(m):
            tot2 = tot[:]
            kk = k
            print(m)
            #for start in range(r+1):
            #extra = 0
            for i in range(len(tot2)):
                extra = 0
                t = tot2[i]
                hm=set()
                if t < m:
                    diff = m-t
                    kk -= diff
                    if kk < 0:
                        return False
                    for j in range(i+1,min(i+r,len(tot2))):
                        if tot2[j]-t > 0:
                            hm.add((j,tot2[j]-t))
                        tot2[j]+=diff
                        
                    for kkk,v in hm:
                        print(kkk,v)
                        for j in range(kkk+1,min(kkk+r,len(tot2))):
                            tot2[j]+=v
                            
                    #for j in range(i-1,max(i-r,-1),-1):
                    #    tot2[j]+=diff

            return True
        
        print(tot)
        print(calculate(138))
        
        l = 0
        
        r = max(tot) + k // len(tot) + 1
        
        ma = 0
        while l < r:
            m = (l+r)//2
            
            if calculate(m):
                ma = max(ma, m)
                l = m + 1
            else:
                r = m 
        
        return ma
        
        #print(tot)
        #print(min(tot))
        
        #hm = {}
        #for i,v in enumerate(tot):
        #    hm[i] = v
        
        small = []
        
        rr = 0
        cm = float('inf')
        for i in range(len(tot)):
            if rr == r:
                cm= min(cm,tot[i])
                small.append(cm)
                cm = float('inf')
                rr = 0
            else:
                cm= min(cm,tot[i])
                rr+=1

        if cm!= float('inf'):
            #if r != rr:
                #small.append(cm)
            #else:
            small[-1] = min(small[-1],cm)
        '''
        
        '''
        rr = 0
        cm = float('inf')
        first = True
        for i in range(len(tot)):
            if rr == r:
                if first:
                    rr = 0
                    continue
                else:
                    cm= min(cm,tot[i])
                    small.append(cm)
                    cm = float('inf')
                    rr = 0
                    first = False
            else:
                cm= min(cm,tot[i])
                rr+=1

        if cm!= float('inf'):
            #if r != rr:
                #small.append(cm)
            #else:
            if small:
                small[-1] = min(small[-1],cm)
            else:
                small.append(cm)
        

        if len(tot) <= 2 *r:
            small = [min(r)]
        else:
            for i in range(r,len(tot)-r):
                sm = float('inf')
                for j in range(1,r):
                    sm = min(sm,sm[i])

        small = sorted(small)
        
        #print(tot)
        #print(small)
        
        mult = 1
        for i in range(len(small)-1):
            if (small[i+1] - small[i]) * mult >= k:
                #print(small[i+1] - small[i])
                return small[i] + k//mult
            
            #print((small[i+1] - small[i]) )
            #print(mult)
            k -= (small[i+1] - small[i]) 
            mult+=1

        #print(k)
        return small[-1] + k//len(small)

        #print(small)
        #small = [ min(v for i,v in enumerate(tot) if i]
        '''
        '''def dp(i):
            if i == len(stations):
                return 0
            
            return min(dp(i) if kk < 0 else float('inf'), dp(i+1)  )
        '''
        
        #return dp(0)
        '''
        def dp(i,kk):
            if i == len(stations):
                return 0
            
            return min(dp(i,) if kk < 0 else float('inf'), dp(i+1)  )
        '''
        
        #return dp(0,0)
        
        