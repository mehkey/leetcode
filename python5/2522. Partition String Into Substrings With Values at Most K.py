class Solution:
    def minimumPartition(self, s: str, k: int) -> int:

        kk = len(str(k)) +1

        @cache
        def dp(i):

            if i == len(s):
                return 0

            m = float("inf")

            for j in range(i+1,min(len(s)+1,i+kk) ):
                if int(s[i:j]) <= k:
                    m =min( m, 1+ dp(j) )

            return m

        res = dp(0) 
        return res if dp(0) != float("inf") else -1
