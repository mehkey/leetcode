class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        nums.sort()
        o = []
        t = []
        m = []
        res = 0
        for n in nums:
            if n % 3 == 0:
                res += n
            elif n%3 == 1:
                o.append(n)
                m.append(n)
            elif n%3 == 2:
                t.append(n)
                m.append(n)
                
        m = m[::-1]
        @cache
        def dp(i,s):
            if i == len(m):
                if s == 0:
                    return 0
                else:
                    return -inf
            
            res = -inf
            
            res = max(res, dp(i+1, (m[i]+s)%3   ) + m[i] , dp(i+1, s) )

            return res
        
        return res + dp(0,0)
        '''
        o = o[::-1]
        t = t[::-1]

        @lru_cache(10_000)
        def dp(i,j):
            if i == len(o) or j == len(t):
                res = 0
            
                if i + 3 <= len(o):
                    res = max(res, dp(i+3,j) + o[i]+ o[i+1]+ o[i+2])

                if j + 3 <= len(t):
                    res = max(res, dp(i,j+3)  + t[j]+ t[j+1]+ t[j+2])
                
                return res

            
            res = 0
            
            if i + 3 <= len(o):
                res = max(res, dp(i+3,j) + o[i]+ o[i+1]+ o[i+2])
            
            if j + 3 <= len(t):
                res = max(res, dp(i,j+3)  + t[j]+ t[j+1]+ t[j+2])
                
            res = max(res, dp(i+1,j+1) + o[i] + t[j])
            
            return res
        
        i = len(o)-1
        j = len(t)-1
        while i >=0 and j >=0:
            
            res += o[i] +t[j]
            i-=1
            j-=1
        
        return res + dp(0,0)
        '''