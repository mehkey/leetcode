class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        N = len(grid[0])
        M = len(grid)

        @cache
        def dp(row, r1, r2):

            if r1 < 0 or r2 < 0 or r1 >= N or r2 >= N:
                return -inf

            if row == M:
                return 0
            
            res = grid[row][r1] + grid[row][r2]

            if r1 == r2:
                res -= grid[row][r2]
            
            extra = 0

            for i in range(r1-1,r1+2):
                for j in range(r2-1,r2+2):
                    extra = max(extra, dp(row+1, i,j))

            return extra + res
        

        return dp(0,0,N-1)



        if grid == [[]]:
            return 0

        m = len(grid)
        n = len(grid[0])

        @lru_cache(None)
        def dfs(row, c1, c2):

            #  Base Case
            if c1 < 0 or c1 >= n or c2 < 0 or c2 >= n:
                return - float("inf")

            res = 0
            res += grid[row][c1] + grid[row][c2]
            
            if c1 == c2:  #   Robots are on the same cell so we subtract one value
                res -= grid[row][c1]

            if row < m - 1:  #  Recursively calling dfs function
                res += max(dfs(row + 1, i, j)
                          for i in [c1 - 1, c1, c1 + 1]
                          for j in [c2 - 1, c2, c2 + 1])

            return res

        return dfs(0, 0, n - 1)