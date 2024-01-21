class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        M = len(s)

        @cache
        def dp(i,k,prev,count):

            if i == M:
                return 0

            res = inf

            
            if k > 0:
                res = min(res, dp(i+1,k-1) + 0 )

            cur = s[i]

            count = 1
            j = i+1
            while j  < M:
                if s[j] == cur:
                    count +=1
                else:
                    break
                j+=1
            
            res = min(res, dp(j,k,cur) + len( str(count)) + 1   )

            res = min(res, dp(i+1,k,cur) + 1)

            return res
        
        return dp(0,k, prev)