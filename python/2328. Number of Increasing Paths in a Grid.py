class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        n, m, mod = len(grid), len(grid[0]), 10**9 + 7
        dp = [[-1] * m for _ in range(n)]
        def dfs(i, j):
            if dp[i][j] != -1: 
                return dp[i][j]
            dp[i][j] = 1
            for r,c in ((0,1),(0,-1),(1,0),(-1,0)):
                if 0 <= i+r < n and 0 <= j+c < m and grid[i][j] < grid[i+r][j+c]:
                    dp[i][j] += dfs(i+r, j+c)
            return dp[i][j]
        
        sum = 0
        for i in range(n):
            for j in range(m):
                sum += dfs(i,j) % mod
        return sum % mod
        #return sum(sum(dfs(i,j) for i in range(n)) % mod for j in range(m)) % mod