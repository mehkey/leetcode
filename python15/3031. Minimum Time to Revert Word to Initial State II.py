class Solution:
    def z_function(self, s):
        z, l, r, n = [0] * len(s), 0, 0, len(s)
        for i in range(1, n):
            if i < r:
                z[i] = min(r - i, z[i - l])

        while i + z[i] < n and s[i + z[i]] == s[z[i]]:
            z[i] += 1

        if i + z[i] > r:
            l, r = i, i + z[i]

        return z

    def minimumTimeToInitialState(self, s: str, k: int) -> int:
        z, n, res = self.z_function(s), len(s), 1

        for i in range(k, n, k):
            if z[i] == n - i:
                return res
            res += 1

        return res
'''
        N = len(word)

        def match(st, hm):
            for w in st:
                hm[w] -=1
            
            for k in hm:
                if hm[k] != 0:
                    return False

            return True
        
        @cache
        def dp(start):
            if start >= N:
                return 0
            
            L = word[start:]

            if L == word[:len(L)] : #and match(word[len(start):],hm):
                return 0

            return dp(start+k)
            
        
        c = Counter()
        
        return dp(k) + 1
        
        
        #@cache
        def dp(start, )
        
            w = 
            if word[:]
        
        
        
        return dp(k, hm ) + 1
        
        w = word

        change = 0

        while True:

            if len(w) >= k:
                w = w[k:] 
            else:
                w = ''

            change += 1
            if w == '' or w == word[:  len(w)]:
                return change
        
        return -1
'''