class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        def min_steps(s):
            l = 0
            r = len(s)-1
            ans = 0
            while l < r:
                if s[l] != s[r]:
                    ans +=1
                l +=1
                r -=1
            return ans


        @cache
        def dp(i, k):
            if i == len(s):
                if k == 0:
                    return 0
                return float("inf")
            if k == 0:
                return float("inf")
            ans = float("inf")
            for j in range(i, len(s)):
                ans = min(ans, min_steps(s[i:j+1]) + dp(j+1, k-1))
            return ans
        
        return dp(0, k)