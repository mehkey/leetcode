def make_nCr_mod(max_n=2 * 10**5, mod=10**9 + 7):
    max_n = min(max_n, mod - 1)

    fact, inv_fact = [0] * (max_n + 1), [0] * (max_n + 1)
    fact[0] = 1
    for i in range(max_n):
        fact[i + 1] = fact[i] * (i + 1) % mod

    inv_fact[-1] = pow(fact[-1], mod - 2, mod)
    for i in reversed(range(max_n)):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod

    @cache
    def nCr_mod(n, r):
        res = 1
        while n or r:
            a, b = n % mod, r % mod
            if a < b:
                return 0
            res = res * fact[a] % mod * inv_fact[b] % mod * inv_fact[a - b] % mod
            n //= mod
            r //= mod
        return res

    return nCr_mod

ccc = make_nCr_mod()

class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        
        #total = borders
        
        left = n - len(sick)
        
        ss = set(sick)
        
        bd = 0
        
        MOD = 10**9+7
        
        '''
        for i in range(0,n):
            if i-1 >= 0 and i-1 in ss:
                bd+=1
            else if i + 1 < n and i+1 in ss:
                bd+=1

        def dp(borders,left):
            if left == 0:
                return 1
            
            return borders * dp( borders -1 , left -1) % MOD
            
        '''
        
        ran = []
        left = 0
        for i in range(len(sick)):
            if sick[i] - left >= 1:
                ran.append([left,sick[i]-1])

            left = sick[i] + 1
        
        if n-1 - left >= 0:
            ran.append([left,n-1])

        
        @cache
        def dp(dis, ll, rr):
            
            if dis == 1:
                return 1

            res = 0

            if ll:
                res += dp(dis-1,ll,rr) % MOD
            if rr:
                res += dp(dis-1,ll,rr) % MOD

            return res % MOD

        res = 1
        
        

        '''
        
        def binomialCoefficient(n, k): 
            # since C(n, k) = C(n, n - k) 
            if(k > n - k): 
                k = n - k 
            # initialize result 
            res = 1
            # Calculate value of  
            # [n * (n-1) *---* (n-k + 1)] / [k * (k-1) *----* 1] 
            for i in range(k): 
                res = res * (n - i) 
                res = res // (i + 1) 
            return res
        '''
        # function to find the binomial coefficient
        @cache
        def binomialCoeff(n, k):
            
            C = [0 for i in range(k + 1)]

            C[0] = 1

            for i in range(1, n + 1, 1):

                # Compute next row of pascal 
                # triangle using the previous row
                j = min(i, k)
                while(j > 0):
                    C[j] = C[j] + C[j - 1] %  MOD
                    j -= 1

            return C[k]
            '''
            mod = MOD
            res = 1
            while n or r:
                a, b = n % mod, r % mod
                if a < b:
                    return 0
                res = res * fact[a] % mod * inv_fact[b] % mod * inv_fact[a - b] % mod
                n //= mod
                r //= mod
            return res

            #return nCr_mod
            '''

        first = True
        llll = 0
        vals = 1
        
        for r in ran:
            ll = r[0] - 1 in ss # != 0
            rr = r[1] + 1 in ss #!= n-1
            diff = r[1]-r[0]+1
            #print(diff,ll,rr)
            val= dp(diff,ll,rr)
            #res += dp(r[1]-r[0],ll,rr) % MOD
            #print('val', val)
            if first:
                vals *= val % MOD
                #res *= val  % MOD
                llll = diff
                first = False
            else:

                vals *= val %  MOD
                #print(val)
                res *= ccc(llll+diff,llll) %  MOD  #binomialCoeff(llll+diff,diff)  % MOD
                #print(res)
                llll += diff

        return res * vals % MOD
