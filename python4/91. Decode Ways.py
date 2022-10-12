class Solution:
    def numDecodings(self, s: str) -> int:

        """
        encoded = 0

        for c in s:
            encoded *= 10
            encoded += int(c)

        #print(encoded)

        #s = list(str(encoded))

        #print(s)
        #print(s)

        res = 0
        cur = []

        @lru_cache(None)
        def dfs(s,i):
            nonlocal res

            if i >= len(s):
                res += 1
                return
                #return res.append(cur.copy())

            for j in range(i,len(s)):
                num = s[i:j+1]

                if int(num) > 26 or int(num) <= 0 or s[i] == '0':
                    return 

                #cur.append(s[i:j+1])
                dfs(s,j+1)
                #cur.pop()

        k =  ''.join(s)

        l = dfs( k , 0)
        print(res)
        return res

        if not s:
            return 0

        dp = [0 for x in range(len(s) + 1)] 

        # base case initialization
        dp[0] = 1 
        dp[1] = 0 if s[0] == "0" else 1   #(1)

        for i in range(2, len(s) + 1): 
            # One step jump
            if 0 < int(s[i-1:i]) <= 9:    #(2)
                dp[i] += dp[i - 1]
            # Two step jump
            if 10 <= int(s[i-2:i]) <= 26: #(3)
                dp[i] += dp[i - 2]

        return dp[len(s)]
        
        
        """
        
        if not s:
            return 0

        dp = [0 for x in range(len(s) + 1)] 

        dp[0] = 1

        dp[1] = 0 if s[0] == "0" else 1

        for i in range(2,len(s)+1):
            if 0 < int(s[i-1:i]) <= 9:
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]

        return dp[len(s)]

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            