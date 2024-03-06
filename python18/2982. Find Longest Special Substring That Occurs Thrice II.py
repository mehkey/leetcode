class Solution:
    def maximumLength(self, s: str) -> int:
        N = len(s)
        
        
        hm = defaultdict(int)
        hmm = defaultdict(list)

        i = 0
        while i < N:
            cc = s[i]
            #hm[(cc,1)] += 1
            hmm[cc].append(1)
            j = i+1
            while j < N:
                if s[j] != cc:
                    break
                #hm[(cc,j - i + 1)] += 1
                hmm[cc].append(j - i + 1)
                j+=1
            i = j

        #print(hm)
        r = -1
        #print(hmm)
        '''for (cc,le),v in hm.items():
            if v > 2:
                r = max(r, le)
        '''
        for k,l in hmm.items():
            l.sort()
            #print(l)
            if len(l) > 2:
                r = max(r, l[-3])
        return r

        @cache
        def dp(i, l, r  ):
            
            
            if i >= N:
                return 0
            
            cur = s[l:r]
            sl = len(cur)
            
            if i + sl > N:
                return 0
            

            if s[i:i+sl] == cur:
                return 1 + dp(i+1, l,r)
            
            return dp(i+1, l,r)

        r = -1
        for i in range(N):
            cc = s[i]
            if dp(i+1, i, i+1)  >= 2 :
                r = max(r, 1)
            for j in range(i+1,N):
                if s[j] != cc:
                    break

                #sub = s[i:j+1]

                if dp(i+1, i, j+1) >= 2:
                    r = max(r, j+1 - i)
        
        return r