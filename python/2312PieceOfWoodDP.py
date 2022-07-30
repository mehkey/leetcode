class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        @lru_cache(None)
        def f(m,n):
            if m==0 or n==0:return 0
            ans=0
            if (m,n) in x:
                ans=x[m,n]
            for j in range(1,m//2+1):
                ans=max(ans,f(j,n)+f(m-j,n))
            for j in range(1,n//2+1):
                ans=max(ans,f(m,j)+f(m,n-j))
            return ans
        x={}
        for a,b,c in prices:
            x[a,b]=c
        return f(m,n)

class Solution:
    def sellingWood(self, m: int, n: int, P: List[List[int]]) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for r, c, p in P:
            dp[r][c] = p
            
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                # Find all the possible first cut:
                for nc in range(1, c // 2 + 1): 
                    dp[r][c] = max(dp[r][c], dp[r][nc] + dp[r][c - nc])
                for nr in range(1, r // 2 + 1):
                    dp[r][c] = max(dp[r][c], dp[nr][c] + dp[r - nr][c])
        print(dp)
        return dp[m][n]