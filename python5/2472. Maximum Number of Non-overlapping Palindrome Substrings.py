class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:

        def checkPal(st):
            return st == st[::-1]
        
        #@lru_cache(1_000_000)
        
        '''
        @cache
        def checkPall(ss):
            return ss == ss[::-1]

        @cache
        def checkPal(i,j):
            ss = s[i:j]

            return checkPall(ss)


        
        dp = [0] * (len(s) + 1)


        for i in range(len(s)-k+1):
            
            if i-1 >= 0:
                dp[i] = max(dp[i], dp[i-1])

            for j in range(i+k, i+k+2 ):

                if j <= len(s) and (j -i) >=k and checkPal(i,j):
                    dp[j] = max(dp[j], 1 + dp[i])
                    break

    
        return max(dp)
        
        
        if len(set( s)) == 1:
            return floor(len(s) /k)
        
        dp = [0] * (len(s) + 1)

        for i in range(len(s)):
            for j in range(len(s) , i, -1):
                
                #tmp = s[i:j]
                #print(tmp)
                if (j -i) >=k and checkPal(i,j):
                    dp[j] = max(dp[j], 1 + dp[i])
                
                if j-1 >= 0:
                    dp[j] = max(dp[j], dp[j-1])
        
        #print(dp)
        return dp[len(s)]

        
            @cache
            def dp(start,end):
                if end < start:
                    return 0

                if end == start:

                    return 0

                ma = 0

                for i in range(start+k,end+1):

                    tmp = s[start:i]

                    if checkPal(tmp):
                        ma = max(ma, 1 + dp(i,end))

                ma = max(ma,dp(start+1,end))

                return ma


            return dp(0,len(s))
        
        
        
        @cache
        def dp(start,end):
            if end < start:
                return 0

            if end == start:

                return 0

            ma = 0

            for i in range(start+k,end+1):

                tmp = s[start:i]

                if checkPal(tmp):
                    ma = max(ma, 1 + dp(i,end))

            ma = max(ma,dp(start+1,end))

            return ma

        return dp(0,len(s))
        '''

        @cache
        def dp(start,end):
            if end < start:
                return 0

            if end == start:
                return 0

            if end > len(s):
                return 0

            ma = 0

            #for i in range(start+k,end+1):

            tmp = s[start:start+k]

            if checkPal(tmp):
                ma = max(ma, 1 + dp(start +k,end))

            ma = max(ma,dp(start+1,end))

            return ma

        return dp(0,len(s))
