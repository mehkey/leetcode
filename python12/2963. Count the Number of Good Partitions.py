class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        N = len(nums)
        hm = defaultdict(list)
        pm = [-1] * N
        ints = []
        s = set()
        for i,nn in enumerate(nums):
            hm[nn].append(i)
            s.add(nn)

        for nn in s:
            ints.append((hm[nn][0],hm[nn][-1]))
        
        ints.sort(key=lambda x :x[0])
        
        st = []
        
        
        for l,r in ints:
            maxr = r
            while st and l <= st[-1][1]:
                ll,rr = st.pop()
                maxr = max(maxr,rr)
            st.append((l,maxr))

        return pow(2, len(st)-1, MOD)

        #print(pm)
        
        #for i in range
        #return 0
        '''
        1234
        
        1 2 3 4
        
        
        1111
        
        1 
        
        
        n = len(nums)
        prevs = [False] * n
        pv =  [False] * n
        pm = [-1] * n

        hm = defaultdict(list)
        hmm = defaultdict(int)

        for i,nn in enumerate(nums):
            prevs[i] = hm[nn][:]
            if hm[nn]:
                #print(hmm[nn])
                #print('vals', hmm.values())
                pm[i] = min(v for v in hmm.values())
                #pm[i] = hmm[nn] #min(v for v in hmm.values())#min([v for v in hm])
                #pm[i] = hm[nn][-1] #min(v for v in hm.values()) #hm[nn][-1]
            else:
                pm[i] = -1
            #if all( v == 0 for v in hm.values()):
            #if len(hm[nn]) > 0:
            #    pv[i] = True
            hm[nn].append(i)
            hmm[nn] = min(hmm.get(nn,inf),i) #max(hmm[nn], i)

        #print(prevs)
        #print(pv)
        print(pm)
        @cache
        def dp(i):
            if i == 0:
                return 1
            #print(i,n)
            #if pv[i] == False:
            #if len(prevs[i]) ==  0:
            if pm[i] == -1:
                return 2* dp(i-1) % MOD
            else:
                return dp(pm[i]) % MOD
            
        return (dp(n-1) ) % MOD
        '''