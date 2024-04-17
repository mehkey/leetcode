

class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        
        pos = set()

        c = Counter(s)
        
        for k,v in c.items():
            v /= 2

        '''
        abc abc
        
        abc
        
        cba
        
        
        0: a:1, b:1, c:1
        1: b:1, c:1
        
        0: a:1, b:1, c:1
        1: a:1, b:1
        
        
        '''
        
       
        res = []
        
        N = len(s)
        L = s[:N//2]
        R = s[N//2::][::-1]
        
        LM = defaultdict(dict)
        
        RM = defaultdict(dict)
        
        #print(L,R)
        #for i in range(L):
        hm = Counter()#defaultdict(int)
        hm2 = Counter()#defaultdict(int)
        LM[-1] = Counter()
        RM[-1] = Counter()
        for i in range(N//2):
            hm[L[i]] += 1
            LM[i] = hm.copy()
            #hm[L[i]] += 1
            hm2[R[i]] += 1
            RM[i] = hm2.copy()
            # hm2[R[i]] += 1
        #print(LM,RM)
        
        @cache
        def eqleft(i):
            for j in range(i+1):
                if L[j] != R[j]:
                    return False
            return True
        
        @cache 
        def eqright(i):
            #print("R", L, R)
            for j in range(i, N//2):
                if L[j] != R[j]:
                    #print("F")
                    return False
            return True
        
        @cache 
        def eqmid(i,k):
            for j in range(i, k+1):
                if L[j] != R[j]:
                    return False
            return True
        
        @cache
        def check(l,r):
            if r <= l:
                return True

            LLM = LM[r] - LM[l-1]
            RRM = RM[r] - RM[l-1]
            
            #print(l,r, LLM, RRM)
            return LLM == RRM

        for a,b,c,d in queries:
            d = N -1 - d 
            c = N -1 - c 
            
            #p1, p2, 
            p1 = min(a, d) 
            p2 = max(b,c) 
            #print(p1,p2)
            #print(a,b,d,c)
            #p3 = 
            if eqleft(p1 -1) and eqright(p2+1) :
                #print("HERE")
                
                if b < d  :
                    #print("THERE")
                    if check(p1,b) and eqmid(b+1,d-1) and check(d, p2):# eqmid(p1, b) and check(b+1,c-1) and eqmid(c, p2):
                        res.append(True)
                    else:
                        res.append(False)
                elif c < a:
                    if check(p1,c) and eqmid(c+1,a-1) and check(a, p2):# eqmid(p1, b) and check(b+1,c-1) and eqmid(c, p2):
                        res.append(True)
                    else:
                        res.append(False)
                else:
                    if check(p1,p2):
                        res.append(True)
                    else:
                        res.append(False)
            else:
                res.append(False)
        return res